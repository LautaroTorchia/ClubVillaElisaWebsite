from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
from flask_migrate import Migrate

db = SQLAlchemy()
from src.core.board.user import User
from src.core.board.discipline import Discipline
from src.core.board.associate import Associate
from src.core.board.role import Role
from src.core.board.payment import Payment
from src.core.board.permission import Permission
migrate = Migrate()

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)
    #db.create_all()

