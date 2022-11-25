import json
import decimal
from src.web.helpers.response_codes import status_msg
from datetime import datetime


class fake_float(float):
    def __init__(self, value):
        """Args:
        value (float): Value to be converted
        """
        self._value = value

    def __repr__(self):
        """Returns:
        str: String representation of the value
        """
        return str(self._value)


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        """Args:
            o (object): Object to encode
        Returns:
            object: Encoded object
        """
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return fake_float(o)


def response(status, data, data_field_name="data"):
    """Args:
        status (int): HTTP status code
        data (dict): Data to be returned
    Returns:
        JSON: Response data
    """
    # transform every value in data to a string
    try:
        data = [{key: str(value) for key, value in object.items()} for object in data]
    except AttributeError:
        pass
    dict = {
        "timestamp": f"{datetime.now()}",
        "status": status,
        "status_msg": status_msg[status][0],  # gets status msg from gist
        f"{data_field_name}": data,
    }
    return json.loads(json.dumps(dict, indent=4, cls=DecimalEncoder))
