from flask import Blueprint, request, render_template, flash, url_for, redirect
from src.web.forms.config import ConfigForm
from src.core.board.repositories.configuration import update_cfg, get_cfg
from src.web.helpers.form_utils import csrf_remover, bool_checker
from src.web.helpers.auth import has_permission

configuration_blueprint = Blueprint(
    "configuration", __name__, url_prefix="/configuracion"
)


@configuration_blueprint.get("/")
@has_permission("configuration_index")
def index():
    """Returns:
    HTML: Form to update configuration.
    """
    return render_template("configuration.html", form=ConfigForm(obj=get_cfg()))


@configuration_blueprint.post("/actualizar")
@has_permission("configuration_update")
def update():
    """Returns:
    HTML: Redirect to configuration list.
    """
    form = ConfigForm(request.form)
    if form.validate():
        form = csrf_remover(request.form)
        form["payment_available"] = bool_checker(form["payment_available"])
        update_cfg(form)
        flash(f"Se actualizo la configuracion", category="alert alert-info")
        return redirect(url_for("configuration.index"))

    return render_template("configuration.html", form=form)
