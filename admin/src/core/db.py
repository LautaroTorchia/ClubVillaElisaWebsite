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
    db.init_app(app)
    config_db(app)
    
def config_db(app):
    @app.before_first_request
    def create_tables():
        db.create_all()
        # Create Admin
        seeds.run()
    
    @app.teardown_appcontext
    def close_session(exception=None):
        db.session.remove()

def reset_db():
    print("   Deleting database...")
    db.drop_all()
    print("   Creating database ...")
    db.create_all()
    print("   All done!")

