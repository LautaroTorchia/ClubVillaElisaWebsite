from flask import Blueprint
from src.web.helpers.build_response import response
from src.core.auth import list_users
from datetime import datetime

user_api_blueprint = Blueprint(
    "user_api", __name__, url_prefix="/api/club/users"
)

@user_api_blueprint.get("/")
def api_all_users():
    return response(200,list(map(lambda x: {x}, list_users())))

@user_api_blueprint.get("/<user_id>")
def api_user(user_id):
    return response(200, {user_id})