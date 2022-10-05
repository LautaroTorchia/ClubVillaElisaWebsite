import json
import decimal
from src.web.helpers.response_codes import status_msg
from datetime import datetime

class fake_float(float):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return str(self._value)

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return fake_float(o)

def response(status, data):
    dict={
        "timestamp":f"{datetime.now()}",
        "status":status,
        "status_msg":status_msg[status][0], # gets status msg from gist
        "data":data
    }
    return json.loads(json.dumps(dict,indent=4,cls=DecimalEncoder))
