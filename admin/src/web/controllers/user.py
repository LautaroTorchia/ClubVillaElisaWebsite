from flask import Blueprint, redirect, url_for, request, render_template, flash
from src.core.auth import create_user, list_users, update_user, delete_user, get_user_by_id, disable_user, enable_user
from src.core.auth.user import User
from src.web.forms.user import UserForm, UpdateUserForm
from passlib.hash import sha256_crypt
from src.web.helpers.form_utils import  csrf_remover
from src.web.helpers.auth import login_required
from src.web.helpers.pagination import pagination_generator

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.get("/")
@login_required
def index():
    #return render_template("user/list.html", users=list_users())


    pairs=[("first_name","Nombre"),("last_name","Apellido"),("email","Email"),("username","Usuario")]

    if request.args.get("search"):
        paginated_query_data = pagination_generator(list_users(request.args.get("column"),request.args.get("search")), request,"users")
    else:
        paginated_query_data = pagination_generator(list_users(), request,"users")

    return render_template("user/list.html",pairs=pairs,**paginated_query_data)






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

@user_blueprint.post("/disable/<id>")
@login_required
def disable(id):
    flash(f"Se deshabilito al usuario satisfactoriamente", category="alert alert-warning")
    disable_user(id)
    return redirect(url_for("user.index"))

#disabling associates
@user_blueprint.post("/enable/<id>")
@login_required
def enable(id):
    flash(f"Se habilito al usuario satisfactoriamente", category="alert alert-warning")
    enable_user(id)
    return redirect(url_for("user.index"))
