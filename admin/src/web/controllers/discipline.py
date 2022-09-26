from flask import Blueprint, render_template
from src.core.board import list_disciplines

discipline_blueprint = Blueprint("discipline", __name__, url_prefix="/discipline")

@discipline_blueprint.route("/")
def index():
    return f"<p>disciplines {list_disciplines()} index<p>"