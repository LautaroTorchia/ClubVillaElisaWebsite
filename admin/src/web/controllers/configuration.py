from flask import Blueprint, request

from src.core.board import (
    get_cfg,
    update_cfg,
    add_cfg,
)
from src.core.board.configuration import Configuration


configuration_blueprint = Blueprint(
    "configuration", __name__, url_prefix="/configuration"
)


@configuration_blueprint.get("/")
def get():
    return f"config: {get_cfg()}"


# TODO discuss if endpoint will be available
@configuration_blueprint.post("/add")
def add():
    configuration = Configuration(request.json)
    added = add_cfg(configuration)
    return f"added configuration: {added}"


@configuration_blueprint.put("/update")
def update():
    configuration = Configuration(request.json)
    updated = update_cfg(configuration)
    return f"updated configuration: {updated}"
