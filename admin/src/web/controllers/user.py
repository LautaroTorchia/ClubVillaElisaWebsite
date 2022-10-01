from flask import Blueprint, redirect, url_for, request, render_template
from src.core.auth import create_user, list_users, update_user, delete_user
from src.core.auth.user import User
from src.web.forms.user import UserForm

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("/")
def index():
    return render_template("user/list.html", users=list_users())

@user_blueprint.get("/add")
def get_add():
    return render_template("user/add.html")

@user_blueprint.post("/add")
def post_add():
    form = UserForm(request.form)
    if form.validate():
        create_user(form)
    return redirect(url_for("user.index"))

@user_blueprint.delete("/delete/<id>")
def delete(id):
    delete_user(id)
    return redirect(url_for("user.index"))

@user_blueprint.post("/modify/<id>")
def modify(id):
    form = UserForm(request.form)
    if form.validate():
        update_user(id, form)
    return redirect(url_for("user.index"))

    