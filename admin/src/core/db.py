from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
from flask_migrate import Migrate

db = SQLAlchemy()
from src.core.board.user import User
migrate = Migrate()

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)
    #db.create_all()

