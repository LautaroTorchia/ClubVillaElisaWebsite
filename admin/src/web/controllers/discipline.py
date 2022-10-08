from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.core.board import list_disciplines, add_discipline, get_discipline, delete_discipline, update_discipline
from src.web.forms.discipline import DisciplineForm
from src.web.helpers.auth import login_required

discipline_blueprint = Blueprint("discipline", __name__, url_prefix="/discipline")


@discipline_blueprint.get("/")
@login_required
def index():
    return render_template("discipline/list.html",disciplines=list_disciplines())

@discipline_blueprint.get("/add")
@login_required
def get_add():
    return render_template("discipline/add.html",form=DisciplineForm())

@discipline_blueprint.post("/add")
@login_required
def post_add():
    form = DisciplineForm(request.form)
    if form.validate():
        add_discipline(form.data)
        return redirect(url_for("discipline.index"))
    else:
        return render_template("discipline/add.html", form=form)

@discipline_blueprint.get("/update/<id>")
@login_required
def get_update(id):
    return render_template("discipline/update.html",form=DisciplineForm(obj=get_discipline(id)))

@discipline_blueprint.post("/update/<id>")
@login_required
def update(id):
    form = DisciplineForm(request.form)
    if form.validate():
        update_discipline(id,form.data)
        return redirect(url_for("discipline.index"))
    else:
        return render_template("discipline/update.html", form=form)

@discipline_blueprint.post("/delete/<id>")
@login_required
def delete(id):
    flash(f"Se elimino {get_discipline(request.form['Delete'])}", category="alert alert-warning")
    delete_discipline(id)
    return redirect(url_for("discipline.index"))

