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
        return payments.paginated_filter(column,filter)
    return payments.paginated_list()