from flask import Blueprint, jsonify
from src.web.helpers.build_response import response
from src.core.board import get_associate_by_id
from src.web.controllers.payments import create

payment_api_blueprint = Blueprint(
    "payment_api", __name__, url_prefix="/me/payments"
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

