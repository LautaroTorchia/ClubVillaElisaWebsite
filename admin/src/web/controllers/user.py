from cmath import e
from sqlite3 import IntegrityError
from flask import Blueprint, redirect, url_for, request, render_template, flash
from src.core.auth import (
    create_user,
    list_users,
    update_user,
    delete_user,
    get_user_by,
    disable_user,
    enable_user,
    add_role_to_user,
    get_roles,
    get_role,
    remove_role_to_user,
)
from src.web.forms.user import UserForm, BasicUserForm
from passlib.hash import sha256_crypt
from src.web.helpers.form_utils import csrf_remover
from src.web.helpers.auth import has_permission
from src.web.helpers.pagination import pagination_generator

user_blueprint = Blueprint("user", __name__, url_prefix="/usuarios")


@user_blueprint.get("/")
@has_permission("user_index")
def index():
    """Returns:
    HTML: List of users.
    """
    pairs = [
        ("name", "Nombre"),
        ("surname", "Apellido"),
        ("email", "Email"),
        ("username", "Usuario"),
        ("true", "Activo"),
        ("false", "Inactivo"),
    ]
    if request.args.get("column") in ["true", "false"]:
        paginated_query_data = pagination_generator(
            list_users("active", request.args.get("column")), request, "users"
        )
    elif request.args.get("search"):
        paginated_query_data = pagination_generator(
            list_users(request.args.get("column"), request.args.get("search")),
            request,
            "users",
        )
    else:
        paginated_query_data = pagination_generator(list_users(), request, "users")

    return render_template("user/list.html", pairs=pairs, **paginated_query_data)


@user_blueprint.get("/agregar")
@has_permission("user_create")
def get_add():
    """Returns:
    HTML: Form to create a user.
    """
    return render_template("user/add.html", form=UserForm(roles=get_roles()))


@user_blueprint.post("/agregar")
@has_permission("user_create")
def post_add():
    """Returns:
    HTML: Redirect to user list.
    """
    form = UserForm(request.form, roles=get_roles())
    if form.validate():
        form_encp = dict(form.data)
        if form_encp["roles"] == []:
            flash(f"Se deben asignar roles al usuario", category="alert alert-warning")
            return render_template("user/add.html", form=UserForm(roles=get_roles()))

        form_encp["password"] = sha256_crypt.encrypt(form_encp["password"])
        user = create_user(form_encp)
        for role in form_encp["roles"]:
            add_role_to_user(user, get_role(role))
        flash("Usuario creado correctamente", "alert alert-info")
        return redirect(url_for("user.index"))

    else:
        return render_template("user/add.html", form=form)


@user_blueprint.get("/actualizar/<id>")
@has_permission("user_update")
def get_update(id):
    """Args:
        id (int): User id.
    Returns:
        HTML: Form to update a user.
    """
    user = get_user_by(value=id)
    form = BasicUserForm(obj=user, roles=get_roles(), user_id=id)
    return render_template("user/update.html", form=form)


@user_blueprint.post("/actualizar/<id>")
@has_permission("user_update")
def post_update(id):
    """Args:
        id (int): User id.
    Returns:
        HTML: Redirect to user list.
    """
    form = BasicUserForm(request.form, roles=get_roles(), user_id=id)
    if form.validate():
        form = csrf_remover(form.data)
        roles_form = form.pop("roles")
        update_user(id, form)
        user = get_user_by(value=id)
        roles = get_roles()
        if roles_form != []:
            for role in roles:
                if role.name in roles_form:
                    add_role_to_user(user, role)
                else:
                    remove_role_to_user(user, role)
        else:
            flash(f"Se deben asignar roles al usuario", category="alert alert-warning")
            return render_template(
                "user/update.html",
                form=BasicUserForm(obj=user, roles=get_roles(), user_id=id),
            )
        flash("Usuario actualizado correctamente", "alert alert-info")
        return redirect(url_for("user.index"))
    return render_template("user/update.html", form=form)


@user_blueprint.post("/borrar/<id>")
@has_permission("user_destroy")
def delete(id):
    """Args:
        id (int): Id of the user to delete.
    Returns:
        HTML: Redirect to user list.
    """
    flash(f"Se elimino al usuario satisfactoriamente", category="alert alert-warning")
    delete_user(id)
    return redirect(url_for("user.index"))


@user_blueprint.post("/desactivar/<id>")
@has_permission("user_update")
def disable(id):
    """Args:
        id (int): Id of the user to disable.
    Returns:
        HTML: Redirect to user list.
    """
    user = get_user_by(value=id)
    for role in user.roles:
        if role.name == "Admin":
            flash(
                f"No se puede desactivar al usuario {user.username} porque es administrador",
                category="alert alert-warning",
            )
            return redirect(url_for("user.index"))
    flash(
        f"Se deshabilito al usuario satisfactoriamente", category="alert alert-warning"
    )
    disable_user(id)
    return redirect(url_for("user.index"))


# disabling associates
@user_blueprint.post("/activar/<id>")
@has_permission("user_update")
def enable(id):
    """Args:
        id (int): Id of the user to enable.
    Returns:
        HTML: Redirect to user list.
    """
    flash(f"Se habilito al usuario satisfactoriamente", category="alert alert-warning")
    enable_user(id)
    return redirect(url_for("user.index"))
