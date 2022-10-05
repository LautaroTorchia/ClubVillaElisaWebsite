from flask import Blueprint,request
from json import dumps
from src.core.board import (
    get_cfg,
    update_cfg,
    add_cfg,
)
from src.web.helpers.build_response import response
from src.core.board.configuration import Configuration
configuration_api_blueprint = Blueprint(
    "configuration_api", __name__, url_prefix="/api/configuracion"
)

@configuration_api_blueprint.get("/")
def get():
    return response(200,get_cfg().as_dict())

@configuration_api_blueprint.put("/update")
def update():
    configuration = Configuration(request.json)
    try:
        updated = update_cfg(configuration)
    except:
        return response(500,"Unexpected error")

    return response(200,updated.as_dict())