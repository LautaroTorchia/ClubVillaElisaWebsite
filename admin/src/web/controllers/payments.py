from datetime import datetime
from core.board.repositories.associate import get_associate_by_id
from core.board.repositories.configuration import get_cfg
from flask import Blueprint, render_template, request, redirect, url_for,flash,send_file
from src.web.helpers.auth import login_required
from src.web.helpers.pagination import pagination_generator
from src.core.board import list_payments,get_last_fee_paid,create_payment,delete_associate,delete_payment
from src.web.helpers.payment_helpers import disciplines_fee_amount

payments_blueprint = Blueprint("payments", __name__, url_prefix="/pagos")


#listing payments
@payments_blueprint.get("/")
@login_required
def index():
    pairs=[("surname","Apellido")]
    if request.args.get("search"):
        paginated_query_data = pagination_generator(list_payments(request.args.get("column"),request.args.get("search")), request,"payments")
    else:
        paginated_query_data = pagination_generator(list_payments(), request,"payments")
    return render_template("payments/list.html", pairs=pairs,**paginated_query_data)


#creating a payment
@payments_blueprint.post("/create/<id>")
@login_required
def create(id):
    associate=get_associate_by_id(id)
    last_fee=get_last_fee_paid(associate)
    config=get_cfg()
    ammount=disciplines_fee_amount(associate)+config.base_fee
    
    if last_fee.installment_number!=0: #if the associate has paid at least one fee
        if last_fee.date.month==datetime.now().month: #if the last fee was paid this month
            flash(f"El asociado ya pago la cuota de este mes", category="alert alert-warning")
            return redirect(url_for("associate.index"))
        elif last_fee.date.month<datetime.now().month-1: #if the last fee was paid more than one month ago
            flash(f"El asociado ha pagado una cuota de un mes anterior", category="alert alert-warning")
            ammount+=config.due_fee
            
    create_payment(associate,ammount,last_fee.installment_number)
    return redirect(url_for("associate.index"))


#deleting a payment
@payments_blueprint.post("/delete/<id>")
@login_required
def delete(id):
    delete_payment(id)
    return redirect(url_for("payments.index"))


#download a payment receipt
@payments_blueprint.get("/download/<id>")
@login_required
def download_receipt(id):
    return send_file("src/web/static/receipts/receipt.pdf",as_attachment=True)