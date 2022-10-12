from flask import Blueprint
from src.web.helpers.build_response import response
from src.core.auth import list_users
from datetime import datetime

user_api_blueprint = Blueprint(
    "user_api", __name__, url_prefix="/api/club/users"
)

@user_api_blueprint.get("/")
def index_api():
    return response(200,list(map(lambda x: {x}, list_users())))