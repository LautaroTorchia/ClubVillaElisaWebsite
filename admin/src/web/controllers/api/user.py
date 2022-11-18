from flask import Blueprint
from src.web.helpers.build_response import response
from src.core.auth import list_users, get_user_by
from datetime import datetime

user_api_blueprint = Blueprint("user_api", __name__, url_prefix="/users")


@user_api_blueprint.get("/")
def api_all_users():
    return response(200, list(map(lambda x: x.to_dict(), list_users(paginate=False))))


@user_api_blueprint.get("/<user_id>")
def api_user(user_id):
    """Args:
        user_id (int): User id
    Returns:
        JSON: User data
    """
    user = get_user_by(value=user_id)
    if user:
        return response(200, user.to_dict().pop("password"))
    return response(404, "No existe el usuario")
