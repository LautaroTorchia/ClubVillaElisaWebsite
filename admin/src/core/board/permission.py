from sqlalchemy import String, Integer, Column
from src.core.db import db


class Permission(db.Model):
    """Permission Model
    Args:
        name (str): Name of permission
    """

    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True)
    name=Column(String)
    # TODO add relation

    def __init__(self, name):
        self.name = name 
    
    def __repr__(self):
        return f"{self.name}"
