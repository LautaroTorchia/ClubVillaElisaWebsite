import os
from flask import Blueprint, render_template, request, redirect, url_for,flash,send_file
from src.core.board import create_associate, delete_associate,get_associate_by_id, list_associates, update_associate,add_discipline_to_associate,list_disciplines,remove_discipline_to_associate,get_discipline
from src.web.forms.associate import CreateAssociateForm, UpdateAssociateForm
from src.web.helpers.writers import write_csv_file,write_pdf_file
from src.web.helpers.auth import login_required
from src.web.helpers.pagination import pagination_generator

associate_blueprint = Blueprint("associate", __name__, url_prefix="/associate")


#Listing associates
@associate_blueprint.route("/")
@login_required
def index():
    pairs=[("surname","Apellido")]
    if request.args.get("search"):
        paginated_query_data = pagination_generator(list_associates(request.args.get("column"),request.args.get("search")), request,"associates")
    else:
        paginated_query_data = pagination_generator(list_associates(), request,"associates")
    return render_template("associate/list.html", pairs=pairs,**paginated_query_data)

#adding associates
@associate_blueprint.get("/add")
@login_required
def get_add():
    return render_template("associate/add.html",form=CreateAssociateForm())

@associate_blueprint.post("/add")
@login_required
def post_add():
    form = CreateAssociateForm(request.form)
    if form.validate():
        associate=create_associate(form.data)
        flash(f"Se agregó {associate}", category="alert alert-info")
        return redirect(url_for("associate.index"))
    return render_template("associate/add.html", form=form)

#deleting associates
@associate_blueprint.post("/delete/<id>")
@login_required
def delete(id):
    flash(f"Se elimino al asociado satisfactoriamente", category="alert alert-warning")
    delete_associate(id)
    return redirect(url_for("associate.index"))

#updating associates
@associate_blueprint.get("/update/<id>")
@login_required
def get_update(id):
    associate=get_associate_by_id(id)
    form=UpdateAssociateForm(obj=associate)
    return render_template("associate/update.html",form=form)

#updating associates
@associate_blueprint.post("/update/<id>")
@login_required
def post_update(id):
    form = UpdateAssociateForm(request.form)
    if form.validate():
        flash(f"Se actualizó {get_associate_by_id(id)}", category="alert alert-info")
        update_associate(form.data,id)
        return redirect(url_for("associate.index"))
    return render_template("associate/add.html", form=form)

#csv_writing associates
@associate_blueprint.get("/csv_writer")
@login_required
def write_csv():
    CSV_PATH=os.path.join(os.getcwd(),"public","Associate_list_report.csv")
    write_csv_file(CSV_PATH,list_associates())
    return send_file(CSV_PATH,as_attachment=True)

#pdf_writing associates
@associate_blueprint.get("/pdf_writer")
@login_required
def write_pdf():
    PDF_PATH=os.path.join(os.getcwd(),"public","Associate_list_report.pdf")
    write_pdf_file(PDF_PATH,list_associates())
    return send_file(PDF_PATH,as_attachment=True)


#add a new discipline to the associate
@associate_blueprint.get("/add_discipline/<id>")
@login_required
def add_discipline(id):
    associate=get_associate_by_id(id)
    return render_template("associate/add_discipline.html",associate=associate,disciplines=list_disciplines())

#add a discipline to the associate
@associate_blueprint.post("/add_discipline/<id>/<discipline_id>")
@login_required
def register_discipline(id,discipline_id):
    associate=get_associate_by_id(id)
    discipline=get_discipline(discipline_id)
    add_discipline_to_associate(associate,discipline)
    flash(f"Se agregó la disciplina {discipline} al asociado {associate}", category="alert alert-info")
    print("ya hice todo")
    return redirect(url_for("associate.add_discipline",id=id))


#delete a discipline from the associate
@associate_blueprint.post("/delete_discipline/<id>/<discipline_id>")
@login_required
def delete_discipline(id,discipline_id):
    associate=get_associate_by_id(id)
    discipline=get_discipline(discipline_id)
    remove_discipline_to_associate(associate,discipline)
    flash(f"Se eliminó la disciplina {discipline} del asociado {associate.name} {associate.surname}", category="alert alert-info")
    return redirect(url_for("associate.add_discipline",id=id))