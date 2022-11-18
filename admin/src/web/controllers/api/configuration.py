from flask import Blueprint, request
from json import dumps
from src.core.board import (
    get_cfg,
    update_cfg,
    add_cfg,
)
from src.web.helpers.build_response import response
from src.core.board.configuration import Configuration

configuration_api_blueprint = Blueprint(
    "configuration_api", __name__, url_prefix="/configuracion"
)


@configuration_api_blueprint.get("/")
def get():
    """Returns:
    JSON: System configuration
    """
    return response(200, get_cfg().to_dict())


@configuration_api_blueprint.put("/update")
def update():
    """Returns:
    JSON: System updated configuration
    """
    configuration = Configuration(request.json)
    try:
        updated = update_cfg(configuration)
    except:
        return response(500, "Unexpected error")

    return response(200, updated.to_dict())
