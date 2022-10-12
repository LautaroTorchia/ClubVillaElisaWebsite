from flask import Blueprint
from src.web.helpers.build_response import response
from src.core.board import list_all_discipolines
from datetime import datetime

discipline_api_blueprint = Blueprint(
    "discipline_api", __name__, url_prefix="/api/club/disciplines"
)

@discipline_api_blueprint.get("/")
def index_api():
    return response(200,list(map(lambda x: x.to_dict(), list_all_discipolines())))