from flask import Blueprint
import src.core.db as database
from flask import current_app as app

resetdb_api_blueprint = Blueprint("resetdb_api", __name__, url_prefix="/resetdb")


@resetdb_api_blueprint.get("/EE7B8DA8E71E36A651E765B88F2A6")
def resetdb():
    with app.app_context():
        database.reset_db()
    return "Database reseted"
