from sqlalchemy import String, Integer, Column, Boolean
from src.core.db import db


class Permission(db.Model):
    """Model for the permissions table.
    Args:
        name (str): The name of the permission.
    """

    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    deleted = Column(Boolean(), default=False)

    def __init__(self, name):
        """Args:
        name (str): The name of the permission.
        """
        self.name = name

    def __repr__(self):
        """Returns:
        str: The string representation of the permission.
        """
        return f"{self.name}"
