from flask import Blueprint
from src.web.helpers.build_response import response
from src.core.board import list_all_disciplines

discipline_api_blueprint = Blueprint(
    "discipline_api", __name__, url_prefix="/disciplines"
)


@discipline_api_blueprint.get("/")
def index_api():
    """Returns:
    JSON: List of disciplines.
    """
    return response(200, list(map(lambda x: x.dict_repr(), list_all_disciplines())))
