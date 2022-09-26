from flask import Blueprint, render_template, request, redirect, url_for
from src.core.board import list_disciplines, add_discipline, get_discipline, delete_discipline, update_discipline
from src.core.board.discipline import Discipline


discipline_blueprint = Blueprint("discipline", __name__, url_prefix="/discipline")


@discipline_blueprint.route("/")
def index():
    return f"<p>disciplines {list_disciplines()} index<p>"


@discipline_blueprint.post("/add")
def add():
    discipline = Discipline(request.json)
    add_discipline(discipline)
    return redirect(url_for("discipline.index"))

@discipline_blueprint.delete("/delete/<id>")
def delete(id):
    delete_discipline(id)
    return redirect(url_for("discipline.index"))