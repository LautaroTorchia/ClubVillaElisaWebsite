def bool_checker(attribute):
    if type(attribute) == bool:
        return attribute
    if type(attribute) == str:
        return True if attribute == "True" else False
    raise ValueError(f"This should be a bool or the str values 'True' o 'False' it was {attribute}")

def csrf_remover(form):
    """Removes the csrf token field from a form

    Args:
        form (InmutableDict): This expects a form from a request

    Returns:
        dict: Returns a dict without the csrf token, be careful, this is not a immutable dict
    """
    try:
        form = dict(form)
        form.pop("csrf_token")
    except:
        pass
    return form