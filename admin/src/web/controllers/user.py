from flask import Blueprint, redirect, url_for, request
from src.core.auth import add_user, list_users, get_user_by_id, delete_user
from src.core.auth.user import User

user_blueprint = Blueprint("user", __name__, url_prefix="/user")

@user_blueprint.route("/")
def index():
    return f"<p>users {list_users()} index<p>"

@user_blueprint.post("/add")
def add():
    user = User(request.json)
    add_user(user)
    return redirect(url_for("user.index"))

@user_blueprint.delete("/delete/<id>")
def delete(id):
    delete_user(id)
    return redirect(url_for("user.index"))