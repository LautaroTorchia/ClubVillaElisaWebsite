from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from src.core.board import list_disciplines, add_discipline, get_discipline, delete_discipline, update_discipline
from src.core.board.discipline import Discipline


discipline_blueprint = Blueprint("discipline", __name__, url_prefix="/discipline")

@discipline_blueprint.route("/api")
def index_api():
    return jsonify(list(map(lambda x: x.to_dict(), list_disciplines())))

@discipline_blueprint.route("/")
def index():
    return render_template("discipline.index",disciplines=list_disciplines())

@discipline_blueprint.post("/add")
def add():
    add_discipline(Discipline(request.json))
    return redirect(url_for("discipline.index"))

@discipline_blueprint.put("/update/<id>")
def update(id):
    update_discipline(id,request.json)
    return redirect(url_for("discipline.index"))

@discipline_blueprint.delete("/delete/<id>")
def delete(id):
    delete_discipline(id)
    return redirect(url_for("discipline.index"))