from flask import Blueprint, render_template, request, redirect, url_for
from src.core.board import create_associate, delete_discipline, list_associates
from src.core.board.associate import Associate
from src.web.forms.associate import CreateAssociateForm

associate_blueprint = Blueprint("associate", __name__, url_prefix="/associate")



#Listing associates
@associate_blueprint.route("/")
def index():
    return render_template("associate/list.html", associates=list_associates())


#adding associates
@associate_blueprint.get("/add")
def get_add():
    return render_template("associate/add.html",form=CreateAssociateForm())

@associate_blueprint.post("/add")
def post_add():
    form = CreateAssociateForm(request.form)
    if form.validate():
        create_associate(form)
        return redirect(url_for("associate.index"))
    return render_template("associate/add.html", form=form)


#deleting associates
@associate_blueprint.delete("/delete/<id>")
def delete(id):
    delete_discipline(id)
    return redirect(url_for("discipline.index"))

#updating associates
@associate_blueprint.get("/modify/<id>")
def modify(id):
    delete_discipline(id)
    return redirect(url_for("discipline.index"))\
        