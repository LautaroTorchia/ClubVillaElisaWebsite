from flask import Blueprint
from src.web.helpers.build_response import response
from src.core.board import get_associate_by_id, get_last_fee_paid
from src.web.helpers.payment_helpers import build_payment
from src.core.board.repositories.payments import create_payment

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
    associate=get_associate_by_id(id)
    last_fee=get_last_fee_paid(associate)  
    flash_number,paid_late,fee_date,amount =build_payment(last_fee,associate)

    associate=get_associate_by_id(id)
    last_fee=get_last_fee_paid(associate)  
    flash_number,paid_late,fee_date,amount =build_payment(last_fee,associate)
    message = ""
    if flash_number==1:
        message = "Pago rechazado"
        status = 400
    else:
        message = "Pago registrado"
        status = 200
        
    create_payment(associate,amount,last_fee.installment_number,paid_late,fee_date)
    return response(status, message)


