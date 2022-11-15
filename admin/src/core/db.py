from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app

db = SQLAlchemy()
from src.core.auth.user import User
from src.core.board.discipline import Discipline
from src.core.board.associate import Associate
from src.core.auth.role import Role
from src.core.board.payment import Payment
from src.core.board.configuration import Configuration
from src.core.auth.permission import Permission
from src.core import seeds


def init_app(app):
    """Args:
    app (Flask): The Flask app.
    """
    db.init_app(app)
    config_db(app)


def config_db(app):
    """Args:
    app (Flask): The Flask app.
    """

    @app.before_first_request
    def create_tables():
        """Create tables in the database."""
        db.create_all()
        # Create Admin
        seeds.run()

    @app.teardown_appcontext
    def close_session(exception=None):
        """Args:
        exception (Exception, optional): The exception that was raised. Defaults to None.
        """
        db.session.remove()


def reset_db():
    """Reset the database."""
    print("   Deleting database...")
    db.session.commit()
    db.drop_all()
    print("   Creating database ...")
    db.create_all()
    print("   All done!")
    seeds.run()
    seeds.populate()
