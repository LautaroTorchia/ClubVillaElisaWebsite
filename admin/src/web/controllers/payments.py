from datetime import datetime
import os
from src.core.board.repositories.configuration import get_cfg
from flask import Blueprint, render_template, request, redirect, url_for,flash,send_file
from src.web.helpers.auth import has_permission, login_required
from src.web.helpers.pagination import pagination_generator
from src.core.board import list_payments,get_last_fee_paid,create_payment,delete_payment,get_payment_by_id,get_associate_by_id,update_payment
from src.web.helpers.payment_helpers import disciplines_fee_amount,make_receipt

payments_blueprint = Blueprint("payments", __name__, url_prefix="/pagos")


#listing payments
@payments_blueprint.get("/")
@login_required
def index():
    """Returns:
        HTML: List of payments.
    """    
    pairs=[("associate.surname","Apellido"),("associate_id","Numero de socio")]
    if request.args.get("search"):
        paginated_query_data = pagination_generator(list_payments(request.args.get("column"),request.args.get("search")), request,"payments")
    else:
        paginated_query_data = pagination_generator(list_payments(), request,"payments")
    return render_template("payments/list.html", pairs=pairs,**paginated_query_data)


#creating a payment
@payments_blueprint.post("/create/<id>")
@login_required
def create(id):
    """Args:
        id (int): id of the associate to create a payment for
    Returns:
        HTML: Redirect to payments list.
    """    
    associate=get_associate_by_id(id)
    last_fee=get_last_fee_paid(associate)
    config=get_cfg()
    amount=disciplines_fee_amount(associate)+config.base_fee
    paid_late=False
    fee_date=datetime.now()
    
    if last_fee.installment_number!=0: #if the associate has paid at least one fee
        
        if last_fee.date.month==datetime.now().month and last_fee.date.year==datetime.now().year: #if the last fee was paid this month
            flash(f"El asociado ya pago la cuota de este mes", category="alert alert-warning")
            return redirect(url_for("associate.index"))
        
        elif (datetime.now()-last_fee.date).days>60: #if the last fee was paid more than one month ago
            flash(f"El asociado ha pagado la cuota del {last_fee.date.replace(month=last_fee.date.month+1).date()}", category="alert alert-warning")
            amount+=amount*(config.due_fee/100)
            fee_date=last_fee.date.replace(month=last_fee.date.month+1)
            paid_late=True
            
        else:
            flash(f"El asociado ha pagado la cuota exitosamente", category="alert alert-warning")
            
    else:
        flash(f"El asociado ha pagado la cuota exitosamente", category="alert alert-warning")
            
    payment=create_payment(associate,amount,last_fee.installment_number,paid_late,fee_date)
    return redirect(url_for("payments.detail_view",id=payment.id))


#deleting a payment
@payments_blueprint.post("/delete/<id>")
@login_required
def delete(id):
    """Args:
        id (int): id of the payment to delete
    Returns:
        HTML: Redirect to payments list.
    """    
    delete_payment(id)
    return redirect(url_for("payments.index"))


#download a payment receipt
@payments_blueprint.post("/download/<id>")
@login_required
def download_receipt(id):
    """Args:
        id (int): id of the payment to download the receipt for
    Returns:
        PNG: Download the receipt.
    """    
    RCPT_PATH=os.path.join(os.getcwd(),"public","receipt.png")
    payment=get_payment_by_id(id)
    make_receipt(payment,RCPT_PATH)
    return send_file(RCPT_PATH,as_attachment=True)


#detail_view of a payment
@payments_blueprint.get("/detail/<id>")
@login_required
def detail_view(id):
    """Args:
        id (int): id of the payment to show the detail view for
    Returns:
        HTML: Detail view of a payment.
    """    
    payment=get_payment_by_id(id)
    return render_template("payments/detail_view.html",payment=payment)

#detail_view of a payment
@payments_blueprint.post("/detail/<id>")
@login_required
def update_amount(id):
    """Args:
        id (int): id of the payment to show the detail view for
    Returns:
        HTML: Detail view of a payment.
    """    
    payment=get_payment_by_id(id)
    update_payment(payment,request.form.get("amount"))
    return redirect(url_for("payments.detail_view",id=payment.id))
