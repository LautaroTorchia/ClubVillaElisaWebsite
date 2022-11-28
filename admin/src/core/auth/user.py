from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from src.core.db import db

user_roles = db.Table(
    "user_roles",
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
)


class User(db.Model):
    """Model for the users table.
    Args:
        username (str): User username
        password (str): User password
        email (str): User email
        name (str): User first name
        surname (str): User last name
        active (bool): User active status (default True)
        deleted (bool): User is deleted
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String())
    username = Column(String())
    password = Column(String())
    active = Column(Boolean(), default=True)
    updated_at = Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_at = Column(db.DateTime, default=datetime.utcnow)
    name = Column(String())
    surname = Column(String())
    deleted = Column(Boolean(), default=False)

    roles = db.relationship("Role", secondary="user_roles", back_populates="users")

    def __init__(self, active=True, **data):
        """Args:
        active (bool, optional): User active status. Defaults to True.
        username (str): User username
        password (str): User password
        email (str): User email
        name (str): User first name
        surname (str): User last name
        active (bool): User active status (default True)
        """
        self.username = data["username"]
        self.password = data["password"]
        self.email = data["email"]
        self.name = data["name"]
        self.surname = data["surname"]
        self.active = active

    def __repr__(self):
        """Returns:
        User: The string representation of the user.
        """
        return f"""{self.username} con el correo {self.email}
                con el nombre {self.name} {self.surname}
                y con el estado {self.active}"""

    def to_dict(self):
        """Returns:
        User: The dictionary representation of the user.
        """
        my_dict = self.__dict__
        del my_dict["_sa_instance_state"]
        return my_dict
