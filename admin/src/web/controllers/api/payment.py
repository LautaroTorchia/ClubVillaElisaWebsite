from flask import Blueprint, redirect, url_for,flash
from src.web.helpers.build_response import response
from src.core.board import create_associate, delete_associate, get_associate_by_id, list_associates, update_associate,add_discipline_to_associate,remove_discipline_to_associate,get_discipline,list_all_associates,list_all_disciplines
from src.web.forms.associate import CreateAssociateForm, UpdateAssociateForm
from src.web.helpers.writers import write_csv_file,write_pdf_file
from src.web.helpers.auth import has_permission
from src.web.helpers.pagination import pagination_generator
from src.web.helpers.associate import no_es_moroso
from src.web.helpers.pagination import pagination_generator

payment_api_blueprint = Blueprint(
    "payment_api", __name__, url_prefix="/payments"
)

#request.form.id
@payment_api_blueprint.get("/<id>")
def associate_payments(id):
    """Args:
        id (int): Associate id
    Returns:
        JSON: List of payments for an associate
    """    
    associate = get_associate_by_id(id)
    payments = associate.payments
    if payments:
        return response(200, list(map(lambda x: x.to_dict(), payments)))
    else:
        return response(200,[])

@payment_api_blueprint.post("/<id>")
def add_payment(id):
    """Args:
        id (int): Associate id
    Returns:
        Str: Success message
    """    
    create(id)
    return response(200, "Pago agregado")


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
            flash(f"El asociado ha pagado una cuota de un mes anterior", category="alert alert-warning")
            amount+=amount*(config.due_fee/100)
            fee_date=last_fee.date.replace(month=last_fee.date.month+1)
            paid_late=True
            
        else:
            flash(f"El asociado ha pagado la cuota exitosamente", category="alert alert-warning")
            
    else:
        flash(f"El asociado ha pagado la cuota exitosamente", category="alert alert-warning")
            
    create_payment(associate,amount,last_fee.installment_number,paid_late,fee_date)
    return redirect(url_for("associate.index"))

