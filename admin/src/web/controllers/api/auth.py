from src.web.helpers.build_response import response
from src.core.auth import get_by_email_and_pwd
from flask import Blueprint,request
from src.web.config import Config
from functools import wraps
import jwt

auth_api_blueprint = Blueprint(
    "auth_api", __name__, url_prefix="/auth"
)

@auth_api_blueprint.post("/")
def post():
    user=get_by_email_and_pwd(request.json["user"], request.json["password"])
    if user:
        encoded_jwt = jwt.encode({"id": f"{user.id}"}, Config.SECRET_KEY, algorithm="HS256")
        return response(200,encoded_jwt,"token")
    else:
        return response(401, "Credenciales incorrectas")
