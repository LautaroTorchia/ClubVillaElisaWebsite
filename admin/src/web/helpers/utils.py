def bool_checker(attribute):
    if type(attribute) == bool:
        return attribute
    if type(attribute) == str:
        return True if attribute == "True" else False
    raise ValueError("This should be a bool or the str values 'True' o 'False'")