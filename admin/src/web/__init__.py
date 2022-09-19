from flask import Flask
from src.web.config import config

def create_app(env="development"):
    app = Flask(__name__)
    app.config.from_object(config[env])

    @app.get("/")
    def home():
        return "Hello, world!"

    return app
