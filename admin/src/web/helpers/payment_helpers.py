import functools

#get disciplines_fee_amount
def disciplines_fee_amount(associate):
    """
        Sum the ammount of all disciplines of an associate   
    """
    return functools.reduce(lambda x,y: x+y.monthly_cost,associate.disciplines,0)