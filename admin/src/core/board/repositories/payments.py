from datetime import datetime
from src.core.board.payment import Payment
from src.core.board import payments
from src.web.helpers.form_utils import bool_checker, csrf_remover


#listing payments
def list_payments(column=None,filter=True):
    """ List all payments
    Returns:
        - List of Payment objects
    """
    if column:
        return payments.paginated_ordered_filter(column,filter,Payment.date.desc())
    return payments.paginated_ordered_list(Payment.date.desc())


#get last fee paid
def get_last_fee_paid(associate):
    """ Get last fee paid
    Returns:
        - Payment object
    """
    payment=payments.query.filter(Payment.associate_id==associate.id).order_by(Payment.date.desc()).first()
    if payment:
        return payment
    return Payment(installment_number=0,date=datetime.now(),amount=0,associate_id=associate.id)

#creating a payment
def create_payment(associate,amount,last_installment,paid_late=False,date=datetime.now()):
    """ Create a payment
    Returns:
        - Payment object
    """
    return payments.add(Payment(associate_id=associate.id,amount=amount,date=date,installment_number=last_installment+1,paid_late=paid_late))

def get_payment_by_id(id):
    """ Get a payment by global id
    Returns:
        - Payment object
    """
    return payments.get(id)

#delete payment
def delete_payment(id):
    """ Delete a payment
    Returns:
        - Payment object
    """
    return payments.delete(id)