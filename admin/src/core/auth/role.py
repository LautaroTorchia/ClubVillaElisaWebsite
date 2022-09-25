from sqlalchemy import String, Integer, Column
from src.core.db import db


class Role(db.Model):
    """Role Model
    Args:
        name (str): Name of role
    """

    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name=Column(String)
    users= db.relationship("User", secondary="user_roles", back_populates="roles")
    # TODO add relation

    def __init__(self, name):
        self.name = name 
    
    def __repr__(self):
        return f"{self.name}"
