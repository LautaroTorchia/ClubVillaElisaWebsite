from flask import Blueprint
from src.web.helpers.build_response import response
from src.core.board import get_associate_by_id, get_last_fee_paid, get_associate_by_DNI
from src.web.helpers.payment_helpers import build_payment
from src.core.board.repositories.payments import create_payment

payment_api_blueprint = Blueprint("payment_api", __name__, url_prefix="/payments")


# request.form.id
@payment_api_blueprint.get("/<id>")
def associate_payments(id):
    """Gets payments from associate
    Args:
        id (int): Associate id
    Returns:
        JSON: List of payments for an associate
    """
    associate = get_associate_by_id(id)
    if not associate:
        return response(404, "No existe el asociado")
    last_fee = get_last_fee_paid(associate)
    payment = build_payment(last_fee, associate)
    payments = list(
        filter(
            lambda x: x["deleted"] == False,
            map(lambda x: x.to_dict(), associate.payments),
        )
    )
    res = {
        "payments": payments,
        "name": associate.name,
        "actual_amount": payment[3],  # amount
        "surname": associate.surname,
        "entry_date": associate.entry_date.strftime("%Y-%m-%d %H:%M:%S.%f"),
    }
    return response(200, res)


@payment_api_blueprint.post("/<id>")
def add_payment(id):
    """Adds a payment to an associate
    Args:
        id (int): Associate id
    Returns:
        JSON: Payment created/error
    """
    associate = get_associate_by_id(id)
    if not associate:
        return response(404, "No existe el asociado")
    last_fee = get_last_fee_paid(associate)
    flash_number, paid_late, fee_date, amount = build_payment(last_fee, associate)

    if flash_number == 1:
        message = "Pago rechazado"
        status = 400
    else:
        message = "Pago registrado"
        status = 200
        create_payment(
            associate, amount, last_fee.installment_number, paid_late, fee_date
        )

    return response(status, message)
