from sqlalchemy import String, Integer, Column
from src.core.db import db

roles_permissions = db.Table(
    "roles_permissions",
    Column("role_id", Integer, db.ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", Integer, db.ForeignKey("permissions.id"), primary_key=True),
)

class Role(db.Model):
    """Role Model
    Args:
        name (str): Name of role
    """

    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    users = db.relationship("User", secondary="user_roles", back_populates="roles")
    permissions = db.relationship("Permission", secondary="roles_permissions", back_populates="roles")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"
