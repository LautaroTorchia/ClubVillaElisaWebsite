from flask import Blueprint, redirect,render_template,request,url_for,flash
from src.core.auth import get_by_usr_and_pwd

auth_blueprint=Blueprint("auth",__name__,url_prefix="/autenticar")

@auth_blueprint.get("/")
def login():
    return render_template("login.html")

@auth_blueprint.post("/authenticate")
def authenticate():
    usr=request.form["username"]
    pwd=request.form["password"]
    user=get_by_usr_and_pwd(usr,pwd)
    if not user:
        flash("Usuario o clave incorrecta.", category="alert alert-warning")
        return redirect(url_for('auth.login'))
    #session["user"]=user.username
    flash("La sesion se inicio correctamente", category="info info-warning")
    return redirect(url_for('home'))

@auth_blueprint.get("/logout")
def logout():
    pass
