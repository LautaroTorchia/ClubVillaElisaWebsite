from datetime import datetime
from src.core.board.repositories.payments import get_last_fee_paid


def is_up_to_date(associate):
    """Returns true if the associate is not in debt"""
    payment = get_last_fee_paid(associate)

    if payment.installment_number == 0:
        if (
            datetime.now().year == associate.entry_date.year
            and datetime.now().month == associate.entry_date.month
        ):
            return True

    elif (
        datetime.now().year == payment.date.year
        and datetime.now().month == payment.date.month
    ):
        return True

    elif (
        datetime.now().year == payment.date.year
        and datetime.now().month == payment.date.month + 1
        and datetime.now().day <= 10
        or datetime.now().year == payment.date.year + 1
        and datetime.now().month + 11 == payment.date.month
        and datetime.now().day <= 10
    ):
        return True

    return False
