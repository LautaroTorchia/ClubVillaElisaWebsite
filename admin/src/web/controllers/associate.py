from flask import Blueprint, render_template, request, redirect, url_for,flash,send_file
from src.core.board import create_associate, delete_associate, delete_discipline, disable_associate, enable_associate, get_associate_by_id, list_associates, update_associate
from src.core.board.associate import Associate
from src.web.forms.associate import CreateAssociateForm, UpdateAssociateForm
from src.web.helpers.form_utils import csrf_remover
from src.web.helpers.csv_writer import write_csv_file

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
@associate_blueprint.post("/delete/<id>")
def delete(id):
    flash(f"Se elimino al asociado satisfactoriamente", category="alert alert-warning")
    delete_associate(id)
    return redirect(url_for("associate.index"))

#updating associates
@associate_blueprint.get("/update/<id>")
def get_update(id):
    associate=get_associate_by_id(id)
    form=UpdateAssociateForm(obj=associate)
    return render_template("associate/update.html",form=form)

#updating associates
@associate_blueprint.post("/update/<id>")
def post_update(id):
    form = UpdateAssociateForm(request.form)
    if form.validate():
        form=csrf_remover(request.form)
        update_associate(form,id)
        return redirect(url_for("associate.index"))
    return render_template("associate/add.html", form=form)

#disabling associates
@associate_blueprint.post("/disable/<id>")
def disable(id):
    flash(f"Se deshabilito al asociado satisfactoriamente", category="alert alert-warning")
    disable_associate(id)
    return redirect(url_for("associate.index"))

#disabling associates
@associate_blueprint.post("/enable/<id>")
def enable(id):
    flash(f"Se habilito al asociado satisfactoriamente", category="alert alert-warning")
    enable_associate(id)
    return redirect(url_for("associate.index"))

#disabling associates
@associate_blueprint.get("/csv_writer")
def write_csv():
    filename = "public/csv/Associate_list_report.csv"
    write_csv_file(filename,list_associates())
    send_file(filename,as_attachment=True)
    return redirect(url_for("associate.index"))