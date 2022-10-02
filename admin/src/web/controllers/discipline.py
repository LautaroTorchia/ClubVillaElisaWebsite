from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from src.core.board import list_disciplines, add_discipline, get_discipline, delete_discipline, update_discipline
from src.core.board.discipline import Discipline
from src.web.forms.discipline import DisciplineForm

discipline_blueprint = Blueprint("discipline", __name__, url_prefix="/discipline")

@discipline_blueprint.route("/api")
def index_api():
    return jsonify(list(map(lambda x: x.to_dict(), list_disciplines())))

@discipline_blueprint.route("/")
def index():
    print(list_disciplines()[0].available)
    print(type(list_disciplines()[0].available))
    return render_template("discipline/list.html",disciplines=list_disciplines())

@discipline_blueprint.get("/add")
def get_add():
    return render_template("discipline/add.html",form=DisciplineForm())

@discipline_blueprint.post("/add")
def post_add():
    print(request.form)
    print(type(request.form["available"]))
    add_discipline(Discipline(request.form))
    return redirect(url_for("discipline.index"))

@discipline_blueprint.put("/update/<id>")
def update(id):
    form = dict(request.form)
    form["available"] = bool_checker(form["available"])
    print(form)
    update_discipline(id,form)
    return redirect(url_for("discipline.index"))

@discipline_blueprint.delete("/delete/<id>")
def delete(id):
    delete_discipline(id)
    return redirect(url_for("discipline.index"))

def bool_checker(attribute):
    if type(attribute) == bool:
        return attribute
    if type(attribute) == str:
        return True if attribute == "True" else False
    raise ValueError("This should be a bool or the str values 'True' o 'False'")