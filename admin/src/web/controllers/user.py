from flask import Blueprint, redirect, url_for, request, render_template, flash
from src.core.auth import create_user, list_users, update_user, delete_user, get_user_by_id
from src.core.auth.user import User
from src.web.forms.user import UserForm, UpdateUserForm
from passlib.hash import sha256_crypt
from src.web.helpers.form_utils import  csrf_remover
from src.web.helpers.auth import login_required

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.get("/")
@login_required
def index():
    return render_template("user/list.html", users=list_users())

@user_blueprint.get("/add")
@login_required
def get_add():
    return render_template("user/add.html", form=UserForm())

@user_blueprint.post("/add")
@login_required
def post_add():
    form = UserForm(request.form)
    if form.validate():
        form_encp=dict(form.data)
        form_encp["password"]=sha256_crypt.encrypt(form_encp["password"])
        create_user(form_encp)
    return redirect(url_for("user.index"))

@user_blueprint.get("/update/<id>")
@login_required
def get_update(id):
    user = get_user_by_id(id)
    form = UpdateUserForm(obj=user)
    return render_template("user/update.html", form=form)

@user_blueprint.post("/update/<id>")
@login_required
def post_update(id):
    form = UpdateUserForm(request.form)
    if form.validate():
        form=csrf_remover(request.form)
        update_user(id, form)
        return redirect(url_for("user.index"))
    return render_template("user/update.html", form=form)

@user_blueprint.post("/delete/<id>")
@login_required
def delete(id):
    flash(f"Se elimino al usuario satisfactoriamente", category="alert alert-warning")
    delete_user(id)
    return redirect(url_for("user.index"))
