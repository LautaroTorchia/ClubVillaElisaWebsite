def bool_checker(attribute):
    print(attribute)
    print("-"*20)
    if type(attribute) == bool:
        return attribute
    if type(attribute) == str:
        return True if attribute == "True" else False
    raise ValueError("This should be a bool or the str values 'True' o 'False'")

def csrf_remover(form):
    """Removes the csrf token field from a form

    Args:
        form (InmutableDict): This expects a form from a request

    Returns:
        dict: Returns a dict without the csrf token, be careful, this is not a immutable dict
    """
    form = dict(form)
    form.pop("csrf_token")
    return form