from sqlalchemy import String, Integer, Column, Boolean
from src.core.db import db

roles_permissions = db.Table(
    "roles_permissions",
    Column("role_id", Integer, db.ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", Integer, db.ForeignKey("permissions.id"), primary_key=True),
)


class Role(db.Model):
    """Model for the roles table.
    Args:
        name (str): The name of the role.
    """

    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    deleted = Column(Boolean(), default=False)

    users = db.relationship("User", secondary="user_roles", back_populates="roles")
    permissions = db.relationship("Permission", secondary="roles_permissions")

    def __init__(self, name):
        """Args:
        name (str): The name of the role.
        """
        self.name = name

    def __repr__(self):
        """Returns:
        str: The string representation of the role.
        """
        return f"{self.name}"
