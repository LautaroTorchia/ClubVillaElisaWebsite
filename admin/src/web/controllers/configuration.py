from flask import Blueprint, request,render_template
from src.web.forms.config import ConfigForm

configuration_blueprint = Blueprint(
    "configuration", __name__, url_prefix="/configuracion"
)

@configuration_blueprint.get("/")
def index():
    return render_template('configuration.html', form=ConfigForm())
