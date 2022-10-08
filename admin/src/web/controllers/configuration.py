from flask import Blueprint, request,render_template
from src.web.forms.config import ConfigForm
from src.web.helpers.auth import login_required

configuration_blueprint = Blueprint(
    "configuration", __name__, url_prefix="/configuracion"
)

@configuration_blueprint.get("/")
@login_required
def index():
    return render_template('configuration.html', form=ConfigForm())
