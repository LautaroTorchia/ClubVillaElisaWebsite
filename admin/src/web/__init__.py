from flask import Flask
from src.web.config import config
import src.core.db as database
from src.web.controllers.discipline import discipline_blueprint

def create_app(env="development"):
    app = Flask(__name__)
    app.config.from_object(config[env])
    app.register_blueprint(discipline_blueprint)

    with app.app_context():
        database.init_app(app)

    @app.get("/")
    def home():
        return "Hello, world!"


    @app.teardown_appcontext
    def shutdown_session(exception=None):
        database.db.session.remove()
    
    @app.cli.command("resetdb")
    def resetdb():
        database.reset_db()


    return app
