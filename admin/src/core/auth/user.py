from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base as Base
from src.core.db import db


user_roles = Table(
    "association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)

class User(db.Model):
    """Modelo de los usuarios del club
    Args:
        username (str): User username
        password (str): User password
        email (str): User email
        first_name (str): User first name
        last_name (str): User last name
        active (bool): User active status (default True)
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    active = Column(Boolean(), default=True)
    updated_at = Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_at = Column(db.DateTime, default=datetime.utcnow)
    first_name = Column(String(255))
    last_name = Column(String(255))
    roles = db.relationship("Role", secondary="user_roles", back_populates="users")

    def __init__(self, username, password, email, first_name, last_name, active=True):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.active = active

    def __repr__(self):
        return f"""{self.username} con el correo {self.email}
                con el nombre {self.first_name} {self.last_name}
                y con el estado {self.active}"""
