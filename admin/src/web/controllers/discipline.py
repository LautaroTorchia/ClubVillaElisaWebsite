from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.core.board import list_disciplines, add_discipline, get_discipline, delete_discipline, update_discipline,get_last_discipline
from src.web.forms.discipline import DisciplineForm
from src.web.helpers.auth import has_permission
from src.web.helpers.pagination import pagination_generator
from src.core.board import get_cfg

discipline_blueprint = Blueprint("discipline", __name__, url_prefix="/discipline")

@discipline_blueprint.get("/")
@has_permission("discipline_index")
def index():
    """Returns:
        HTML: List of disciplines.
    """    
    pairs=[("name","Nombre"),("category","Categoría"),("instructors","Instructores"),
    ("dates","Días y horarios"),("true","Disponible"),("false","No Disponible"),("monthly_cost","Costo mensual")]

    if request.args.get("column") in ["true","false"]:
        paginated_query_data = pagination_generator(list_disciplines("available",request.args.get("column")), request,"disciplines")
    elif request.args.get("search"):
        paginated_query_data = pagination_generator(list_disciplines(request.args.get("column"),request.args.get("search")), request,"disciplines")
    else:
        paginated_query_data = pagination_generator(list_disciplines(), request,"disciplines")

    return render_template("discipline/list.html",pairs=pairs,**paginated_query_data)

@discipline_blueprint.get("/add")
@has_permission("discipline_create")
def get_add():
    """Returns:
        HTML: Form to create a discipline.
    """    
    return render_template("discipline/add.html",form=DisciplineForm(currency=get_cfg().currency))

@discipline_blueprint.post("/add")
@has_permission("discipline_create")
def post_add():
    """Returns:
        HTML: Redirect to discipline list.
    """    
    form = DisciplineForm(request.form)
    if form.validate():
        add_discipline(form.data,get_cfg().currency)
        flash(f"Se agregó {get_last_discipline()}", category="alert alert-info")
        return redirect(url_for("discipline.index"))
    else:
        return render_template("discipline/add.html", form=form)

@discipline_blueprint.get("/update/<id>")
@has_permission("discipline_update")
def get_update(id):
    """Args:
        id (int): id of the discipline
    Returns:
        HTML: Form to update a discipline.
    """    
    return render_template("discipline/update.html",form=DisciplineForm(obj=get_discipline(id),currency=get_cfg().currency))

@discipline_blueprint.post("/update/<id>")
@has_permission("discipline_update")
def update(id):
    """Args:
        id (int): id of the discipline
    Returns:
        HTML: Redirect to discipline list.
    """    
    form = DisciplineForm(request.form)
    if form.validate():
        flash(f"Se actualizó {get_discipline(id)}", category="alert alert-info")
        update_discipline(id,form.data)
        return redirect(url_for("discipline.index"))
    else:
        return render_template("discipline/update.html", form=form)

@discipline_blueprint.post("/delete/<id>")
@has_permission("discipline_destroy")
def delete(id):
    """Args:
        id (int): id of the discipline
    Returns:
        HTML: Redirect to discipline list.
    """    
    flash(f"Se elimino {get_discipline(request.form['Delete'])}", category="alert alert-warning")
    delete_discipline(id)
    return redirect(url_for("discipline.index"))

