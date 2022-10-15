
from datetime import datetime
from src.core.board.repositories.payments import get_last_fee_paid


def no_es_moroso(associate):
    payment=get_last_fee_paid(associate)
    if payment.installment_number==0:
        if (datetime.now()-associate.entry_date).days<60:
            return True
        
    elif (datetime.now()-payment.date).days<60:
        return True
    
    return False