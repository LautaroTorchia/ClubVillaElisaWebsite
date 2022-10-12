from flask import Blueprint, jsonify
from src.web.helpers.build_response import response
from src.core.board import list_disciplines,get_associate_by_id
from datetime import datetime

associate_api_blueprint = Blueprint(
    "associate_api", __name__, url_prefix="/api/me/disciplines"
)

@associate_api_blueprint.get("/<id>")
def index_api(id):
    associate=get_associate_by_id(id)
    if associate.disciplines:
        #transform associates IntrumentedLIst into dict
        disciplines=[{"name":discipline.name,
                      "days":discipline.dates,"time":discipline.dates,"teacher":discipline.instructors,
                      "price":discipline.monthly_cost} 
                     for discipline in associate.disciplines]
        return response(200,disciplines)
    else:
        return response(200,[])