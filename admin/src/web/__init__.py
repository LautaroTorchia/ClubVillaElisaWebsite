from flask import Flask
from src.web.config import config
from src.core.db import db, init_db

def create_app(env="development"):
    app = Flask(__name__)
    app.config.from_object(config[env])
    with app.app_context():
        init_db(app)

    @app.get("/")
    def home():
        return "Hello, world!"
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()
    
    return app
