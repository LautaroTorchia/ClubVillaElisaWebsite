from flask import Flask, render_template
from src.web.config import get_config
from src.core.db import db, init_db
from src.web.helpers import handlers

def create_app(env="development", static_url_path="/static", template_folder="templates"):
    config = get_config()
    app = Flask(__name__, static_url_path=static_url_path, template_folder=template_folder)
    
    app.config.from_object(config[env])

    with app.app_context():
        init_db(app)

    @app.get("/")
    def home():
        return render_template('index.html')
    @app.get("/listado_socios")
    def listado_socios():
        return render_template('listado_socios.html')
    @app.get("/configuracion")
    def configuracion():
        return render_template('configuracion.html')
    @app.get("/public_index")
    def public_home():
        return render_template('public_index.html')
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    app.register_error_handler(400, handlers.bad_request_error)
    app.register_error_handler(401, handlers.unauthorized_error)
    app.register_error_handler(403, handlers.forbidden_error)
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)

    return app
