from flask import Flask
from src.web.config import config
from src.core import db

def create_app(env="development"):
    app = Flask(__name__)
    app.config.from_object(config[env])
    with app.app_context():
        db.init_app(app)

    @app.get("/")
    def home():
        return "Hello, world!"
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()
    
    @app.cli.command("resetdb")
    def resetdb():
        db.reset_db()


    return app
