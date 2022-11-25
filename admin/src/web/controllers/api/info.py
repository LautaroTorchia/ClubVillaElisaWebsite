from flask import Blueprint
from src.web.helpers.build_response import response
from src.core.board import get_cfg

info_api_blueprint = Blueprint("info_api", __name__, url_prefix="/info")


@info_api_blueprint.get("/")
def index_api():
    """Returns:
    JSON: Information about the club.
    """
    return response(200, {"Contacto": get_cfg().contact})
