from flask import Blueprint, redirect, render_template, request, url_for, flash, session
from src.core.auth import get_by_usr_and_pwd
from src.web.helpers.auth import login_required, check_logged
from src.web.forms.login import LoginForm

auth_blueprint = Blueprint("auth", __name__, url_prefix="/autenticar")


@auth_blueprint.get("/")
@check_logged
def login():
    """Returns:
    HTML: Login form.
    """
    return render_template("login.html", form=LoginForm())


@auth_blueprint.post("/iniciarSesion")
@check_logged
def authenticate():
    """Returns:
    HTML: Redirect to index.
    """
    form = LoginForm(request.form)
    if form.validate():
        usr = request.form["username"]
        pwd = request.form["password"]
        user = get_by_usr_and_pwd(usr, pwd)
        if not user:
            flash("Usuario o clave incorrecta.", category="alert alert-danger")
            return redirect(url_for("auth.login"))
        if not user.active:
            flash("Usuario inactivo.", category="alert alert-danger")
            return redirect(url_for("auth.login"))
        session["user"] = user.id
        flash("La sesion se inicio correctamente", category="alert alert-success")
    return redirect(url_for("home"))


@auth_blueprint.get("/cerrarSesion")
@login_required
def logout():
    """Returns:
    HTML: Redirect to login.
    """
    del session["user"]
    session.clear()
    return redirect(url_for("auth.login"))
