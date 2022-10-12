from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.core.board import list_disciplines, add_discipline, get_discipline, delete_discipline, update_discipline,get_last_discipline
from src.web.forms.discipline import DisciplineForm
from src.web.helpers.auth import login_required
from src.core.board import get_cfg

discipline_blueprint = Blueprint("discipline", __name__, url_prefix="/discipline")

def pagination_setter(paginator, request, paginator_name="paginator"):
        args = dict(request.args)
        try:
            args.pop("page")
        except KeyError:
            pass
        pages_urls = [(url_for(request.endpoint, page=page_num, **args),page_num) for page_num in paginator.iter_pages(100,100,100,100) ]
        next_url = url_for(request.endpoint, page=paginator.next_num, **args) if paginator.has_next else None
        prev_url = url_for(request.endpoint, page=paginator.prev_num, **args)  if paginator.has_prev else None
        return {"next_url":next_url, "pages_urls":pages_urls, "prev_url":prev_url, f"{paginator_name}":paginator}

@discipline_blueprint.get("/")
@login_required
def index():
    pairs=[("name","Nombre"),("category","Categoría"),("instructors","Instructores"),
    ("dates","Días y horarios"),("true","Disponible"),("false","No Disponible"),("monthly_cost","Costo mensual")]

    if request.args.get("column") in ["true","false"]:
        paginated_query_data = pagination_setter(list_disciplines("available",request.args.get("column")), request,"disciplines")
    elif request.args.get("search"):
        paginated_query_data = pagination_setter(list_disciplines(request.args.get("column"),request.args.get("search")), request,"disciplines")
    else:
        paginated_query_data = pagination_setter(list_disciplines(), request,"disciplines")
        
    return render_template("discipline/list.html",pairs=pairs,**paginated_query_data)

@discipline_blueprint.get("/add")
@login_required
def get_add():
    return render_template("discipline/add.html",form=DisciplineForm(currency=get_cfg().currency))

@discipline_blueprint.post("/add")
@login_required
def post_add():
    form = DisciplineForm(request.form)
    if form.validate():
        add_discipline(form.data,get_cfg().currency)
        flash(f"Se agregó {get_last_discipline()}", category="alert alert-info")
        return redirect(url_for("discipline.index"))
    else:
        return render_template("discipline/add.html", form=form)

@discipline_blueprint.get("/update/<id>")
@login_required
def get_update(id):
    return render_template("discipline/update.html",form=DisciplineForm(obj=get_discipline(id),currency=get_cfg().currency))

@discipline_blueprint.post("/update/<id>")
@login_required
def update(id):
    form = DisciplineForm(request.form)
    if form.validate():
        flash(f"Se actualizó {get_discipline(id)}", category="alert alert-info")
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

