from sqlalchemy import Column, String, Integer, Numeric, Boolean
from src.core.db import db
from src.core.board.base_model import BaseModel


class Discipline(BaseModel):
    """Modelo de las disciplinas del club
    Args:
        name (str): Discipline name
        category (str): Discipline category
        instructors (str): Discipline instructors
        dates (str): Discipline dates and times
        monthly_cost (str): Discipline monthly cost
        available (bool): Discipline availability
    """

    __tablename__ = "disciplines"
    id = Column(Integer, primary_key=True)
    name = Column(String())
    category = Column(String())
    instructors = Column(String())
    dates = Column(String())
    monthly_cost = Column(Numeric())
    available = Column(Boolean())
    deleted = Column(Boolean(), default=False)
    created_at = Column(db.DateTime, default=db.func.now())
    updated_at = Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    associates = db.relationship(
        "Associate", secondary="associate_disciplines", back_populates="disciplines"
    )

    def __init__(self, discipline_data):
        self.name = discipline_data["name"]
        self.category = discipline_data["category"]
        self.instructors = discipline_data["instructors"]
        self.dates = discipline_data["dates"]
        self.monthly_cost = discipline_data["monthly_cost"]
        self.available = discipline_data["available"]

    def __repr__(self):
        return f"""{self.name} en la categoría {self.category} 
        con los instructores {self.instructors} 
        con un costo de {self.monthly_cost} disponible en los días y horarios {self.dates}"""

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "instructors": self.instructors,
            "dates": self.dates,
            "monthly_cost": self.monthly_cost,
            "available": self.available,
            "deleted": self.deleted,
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "updated_at": self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
        }

    def dict_repr(self, costs=False):
        reqs_api_dict = {
            "name": self.name,
            "teacher": self.instructors,
            "dates": self.dates,
        }

        private_api_dict = {
            "name": self.name,
            "teacher": self.instructors,
            "dates": self.dates,
            "category": self.category,
            "monthly_cost": self.monthly_cost,
        }
        return private_api_dict if costs else reqs_api_dict
