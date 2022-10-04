from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from src.core.board import list_disciplines, add_discipline, get_discipline, delete_discipline, update_discipline
from src.core.board.discipline import Discipline
from src.web.forms.discipline import DisciplineForm
from src.web.helpers.utils import bool_checker

discipline_blueprint = Blueprint("discipline", __name__, url_prefix="/discipline")

@discipline_blueprint.route("/api")
def index_api():
    return jsonify(list(map(lambda x: x.to_dict(), list_disciplines())))

@discipline_blueprint.get("/")
def index():
    return render_template("discipline/list.html",disciplines=list_disciplines())

@discipline_blueprint.get("/add")
def get_add():
    return render_template("discipline/add.html",form=DisciplineForm())

@discipline_blueprint.post("/add")
def post_add():
    print(request.form)
    add_discipline(Discipline(request.form))
    return redirect(url_for("discipline.index"))

@discipline_blueprint.get("/update/<id>")
def get_update(id):
    return render_template("discipline/update.html",form=DisciplineForm(obj=get_discipline(id)))

@discipline_blueprint.post("/update/<id>")
def update(id):
    form = dict(request.form)
    form.pop("csrf_token")
    form["available"] = bool_checker(form["available"])
    update_discipline(id,form)
    return redirect(url_for("discipline.index"))

@discipline_blueprint.post("/delete/<id>")
def delete(id):
    flash(f"Se elimino {get_discipline(request.form['Delete'])}", category="alert alert-warning")
    delete_discipline(id)
    return redirect(url_for("discipline.index"))

