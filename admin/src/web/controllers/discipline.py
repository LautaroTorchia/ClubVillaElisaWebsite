from flask import Blueprint, render_template, request
from src.core.board import list_disciplines, add_discipline
from src.core.board.discipline import Discipline


discipline_blueprint = Blueprint("discipline", __name__, url_prefix="/discipline")


@discipline_blueprint.route("/")
def index():
    return f"<p>disciplines {list_disciplines()} index<p>"


@discipline_blueprint.post("/add")
def add():
    discipline = Discipline(request.json)
    add_discipline(discipline)
