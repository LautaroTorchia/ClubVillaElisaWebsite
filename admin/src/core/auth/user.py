from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from src.core.db import db


user_roles = db.Table(
    "user_roles",
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
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
        deleted (bool): User is deleted
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
    deleted = Column(Boolean(), default=False)

    roles = db.relationship("Role", secondary="user_roles", back_populates="users")

    def __init__(self, active=True, **data):
        self.username = data["username"]
        self.password = data["password"]
        self.email = data["email"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.active = active

    def __repr__(self):
        return f"""{self.username} con el correo {self.email}
                con el nombre {self.first_name} {self.last_name}
                y con el estado {self.active}"""
    
    def to_dict(self):
        my_dict = self.__dict__
        del my_dict['_sa_instance_state']
        return my_dict
