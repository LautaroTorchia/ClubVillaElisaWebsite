from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return "Hello, world!"

    return app
