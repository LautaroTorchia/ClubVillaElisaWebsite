from datetime import datetime
from src.core.board.repositories.payments import get_last_fee_paid


def is_up_to_date(associate):
    """Returns true if the associate is not in debt
    """    
    payment=get_last_fee_paid(associate)
    
    if payment.installment_number==0:
        if (datetime.now()-associate.entry_date).days<30:
            return True
        
    elif (datetime.now().month==payment.date.month):
        return True
    
    elif (datetime.now().month==payment.date.month+1 and datetime.now().day<=10):
        return True
    
    return False