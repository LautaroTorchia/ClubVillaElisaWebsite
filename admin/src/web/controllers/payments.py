from datetime import datetime
import os
from src.core.board.repositories.configuration import get_cfg
from flask import Blueprint, render_template, request, redirect, url_for,flash,send_file
from src.web.helpers.auth import login_required
from src.web.helpers.pagination import pagination_generator
from src.core.board import list_payments,get_last_fee_paid,create_payment,delete_payment,get_payment_by_id,get_associate_by_id
from src.web.helpers.payment_helpers import disciplines_fee_amount,make_receipt

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
        else:
            flash(f"El asociado ha pagado la cuota exitosamente", category="alert alert-warning")
    else:
        flash(f"El asociado ha pagado la cuota exitosamente", category="alert alert-warning")
            
    create_payment(associate,ammount,last_fee.installment_number)
    return redirect(url_for("associate.index"))


#deleting a payment
@payments_blueprint.post("/delete/<id>")
@login_required
def delete(id):
    delete_payment(id)
    return redirect(url_for("payments.index"))


#download a payment receipt
@payments_blueprint.post("/download/<id>")
@login_required
def download_receipt(id):
    RCPT_PATH=os.path.join(os.getcwd(),"public","receipt.png")
    payment=get_payment_by_id(id)
    make_receipt(payment,RCPT_PATH)
    return send_file(RCPT_PATH,as_attachment=True)