from flask import Flask
from src.web.config import config
from src.core.db import database, init_app

def create_app(env="development"):
    app = Flask(__name__)
    app.config.from_object(config[env])
    with app.app_context():
        init_app(app)

    @app.get("/")
    def home():
        return "Hello, world!"
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        database.session.remove()
    
    @app.cli.command("reset-db")
    def reset_db():
        database.reset_db()

    return app
