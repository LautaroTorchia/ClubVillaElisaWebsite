from flask import Flask, render_template
from src.web.config import get_config
import src.core.db as database
from src.core import seeds
from src.web.controllers.discipline import discipline_blueprint
from src.web.controllers.associate import associate_blueprint
from src.web.controllers.configuration import configuration_blueprint
from src.web.controllers.api.configuration import configuration_api_blueprint
from src.web.controllers.api.discipline import discipline_api_blueprint
from src.web.controllers.api.associate import associate_api_blueprint
from src.web.controllers.user import user_blueprint
from src.web.controllers.auth import auth_blueprint
from src.web.helpers import handlers, auth
from flask_session import Session


def create_app(env="development", static_folder="/static", template_folder="templates"):

    app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

    # load config
    config = get_config()
    app.config.from_object(config[env])

    # init db
    with app.app_context():
        database.init_app(app)
        # Create Admin
        seeds.run()
    

    # Session
    Session(app)

    # Controllers
    app.register_blueprint(discipline_blueprint)
    app.register_blueprint(associate_blueprint)
    app.register_blueprint(configuration_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)

    # Api
    discipline_api_blueprint
    app.register_blueprint(configuration_api_blueprint)
    app.register_blueprint(discipline_api_blueprint)
    app.register_blueprint(associate_api_blueprint)

    # Routes
    @app.get("/")
    def home():
        return render_template("home.html")

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        database.db.session.remove()

    @app.cli.command("resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command("seeds")
    def seedsdb():
        seeds.run()

    @app.cli.command("populate")
    def populatedb():
        seeds.populate()
        
    # error handlers
    app.register_error_handler(400, handlers.bad_request_error)
    app.register_error_handler(401, handlers.unauthorized_error)
    app.register_error_handler(403, handlers.forbidden_error)
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)

    # Jinja
    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)

    return app
