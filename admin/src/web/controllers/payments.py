from datetime import datetime
import os
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_file,
    session,
)
from src.web.helpers.auth import has_permission
from src.web.helpers.pagination import pagination_generator
from src.core.board import (
    list_payments,
    get_last_fee_paid,
    create_payment,
    delete_payment,
    get_payment_by_id,
    get_associate_by_id,
    update_payment,
)
from src.web.helpers.payment_helpers import make_receipt, build_payment
from src.web.forms.payments import PaymentUpdateForm
from src.web.helpers.form_utils import bool_checker
from sqlalchemy.sql.expression import cast
from sqlalchemy import String
from src.core.board import get_cfg, payments
from src.core.board.associate import Associate

payments_blueprint = Blueprint("payments", __name__, url_prefix="/pagos")


# listing payments
@payments_blueprint.get("/")
@has_permission("payments_index")
def index():
    """Returns:
    HTML: List of payments.
    """
    pairs = [("surname", "Apellido"), ("associate_id", "Numero de socio")]

    if request.args.get("search"):
        if request.args.get("column") == "associate_id":
            paginated_query_data = pagination_generator(
                list_payments(request.args.get("column"), request.args.get("search")),
                request,
                "payments",
            )

        if request.args.get("column") == "surname":
            paginated_query_data = pagination_generator(
                list_payments(
                    request.args.get("column"), request.args.get("search"), Associate
                ),
                request,
                "payments",
            )

    else:
        paginated_query_data = pagination_generator(
            list_payments(), request, "payments"
        )

    return render_template(
        "payments/list.html",
        pairs=pairs,
        **paginated_query_data,
        currency=get_cfg().currency,
    )


# deleting a payment
@payments_blueprint.post("/borrar/<id>")
@has_permission("payments_destroy")
def delete(id):
    """Args:
        id (int): id of the payment to delete
    Returns:
        HTML: Redirect to payments list.
    """
    delete_payment(id)
    return redirect(url_for("payments.index"))


# download a payment receipt
@payments_blueprint.post("/descargar/<id>")
@has_permission("payments_import")
def download_receipt(id):
    """Args:
        id (int): id of the payment to download the receipt for
    Returns:
        PNG: Download the receipt.
    """
    RCPT_PATH = os.path.join(os.getcwd(), "public", "recibo.png")
    payment = get_payment_by_id(id)
    make_receipt(payment, RCPT_PATH)
    return send_file(RCPT_PATH, as_attachment=True)


# confirm a payment
@payments_blueprint.get("/confirmar/<id>")
@has_permission("payments_create")
def confirm_payment_get(id):
    """Args:
        id (int): id of the associate to confirm
    Returns:
        HTML: render to payment detail view.
    """
    associate = get_associate_by_id(id)
    last_fee = get_last_fee_paid(associate)
    flash_number, paid_late, fee_date, amount = build_payment(last_fee, associate)

    if flash_number == 1:
        flash(
            f"El asociado ya pago la cuota de este mes", category="alert alert-warning"
        )
        return redirect(url_for("associate.index"))

    form = PaymentUpdateForm(
        name=associate.name,
        surname=associate.surname,
        date=fee_date.strftime("%m-%Y"),
        amount=amount,
        paid_late=paid_late,
        installment_number=last_fee.installment_number,
        tipo_de_moneda=get_cfg().currency,
    )

    session["data"] = {
        "name": associate.name,
        "surname": associate.surname,
        "date": fee_date,
        "paid_late": paid_late,
        "installment_number": last_fee.installment_number,
        "tipo_de_moneda": get_cfg().currency,
    }

    return render_template(
        "payments/confirm.html", form=form, associate=associate, paid_late=paid_late
    )


# confirm a payment
@payments_blueprint.post("/confirmar/<id>")
@has_permission("payments_create")
def confirm_payment_post(id):
    """Args:
        id (int): id of the associate to confirm
    Returns:
        HTML: Redirect to payment detail view.
    """
    data = session["data"]
    form = PaymentUpdateForm(
        request.form,
        name=data["name"],
        surname=data["surname"],
        date=data["date"].strftime("%m-%Y"),
        paid_late=data["paid_late"],
        installment_number=data["installment_number"],
        tipo_de_moneda=data["tipo_de_moneda"],
    )
    associate = get_associate_by_id(id)

    if form.validate():
        create_payment(
            associate,
            form.data.get("amount"),
            data["installment_number"],
            bool_checker(data["paid_late"]),
            data["date"],
        )
        flash(f"El pago se ha registrado correctamente", category="alert alert-success")
        del session["data"]
        return redirect(url_for("payments.index"))

    return render_template("payments/confirm.html", form=form, associate=associate)


# detail_view of a payment
@payments_blueprint.get("/detalle/<id>")
@has_permission("payments_show")
def detail_view(id):
    """Args:
        id (int): id of the payment to show the detail view for
    Returns:
        HTML: Detail view of a payment.
    """
    payment = get_payment_by_id(id)
    form = PaymentUpdateForm(
        name=payment.associate.name,
        surname=payment.associate.surname,
        date=payment.date.strftime("%m-%y"),
        amount=payment.amount,
        paid_late=payment.paid_late,
        installment_number=payment.installment_number,
        tipo_de_moneda=get_cfg().currency,
    )
    return render_template(
        "payments/detail_view.html",
        payment=payment,
        form=form,
        paid_late=payment.paid_late,
    )
