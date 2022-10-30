from src.core.board import associate_disciplines,Associate,Discipline,associates, list_all_associates
from src.web.helpers.auth import jwt_required
from flask import Blueprint, jsonify
from src.core.db import db

statistics_api_blueprint = Blueprint("statistics_api", __name__, url_prefix="/stats")


@jwt_required
@statistics_api_blueprint.get("/")
def disciplines_by_gender():
    return jsonify( list(filter(lambda elem:elem, map(lambda x: {"associate":x.to_dict(),"disciplines":list(map(lambda d:d.to_dict(), x.disciplines))} if x.disciplines else None,list_all_associates()))))