from flask import Blueprint, redirect, url_for, request, render_template, flash
from src.core.auth import create_user, list_users, update_user, delete_user, get_user_by_id
from src.core.auth.user import User
from src.web.forms.user import UserForm, UpdateUserForm
from passlib.hash import sha256_crypt
from src.web.helpers.form_utils import  csrf_remover

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.get("/")
def index():
    return render_template("user/list.html", users=list_users())

@user_blueprint.get("/add")
def get_add():
    return render_template("user/add.html", form=UserForm())

@user_blueprint.post("/add")
def post_add():
    form = UserForm(request.form)
    if form.validate():
        form_encp=dict(form.data)
        form_encp["password"]=sha256_crypt.encrypt(form_encp["password"])
        create_user(form_encp)
    return redirect(url_for("user.index"))

@user_blueprint.get("/update/<id>")
def get_update(id):
    user = get_user_by_id(id)
    form = UpdateUserForm(obj=user)
    return render_template("user/update.html", form=form)

@user_blueprint.post("/update/<id>")
def post_update(id):
    form = UpdateUserForm(request.form)
    if form.validate():
        form=csrf_remover(request.form)
        update_user(id, form)
        return redirect(url_for("user.index"))
    return render_template("user/update.html", form=form)

@user_blueprint.post("/delete/<id>")
def delete(id):
    flash(f"Se elimino al usuario satisfactoriamente", category="alert alert-warning")
    delete_user(id)
    return redirect(url_for("user.index"))
