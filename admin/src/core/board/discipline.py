from sqlalchemy import Column, String, Integer, Numeric, Boolean
from src.core.db import db


class Discipline(db.Model):
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
    name = Column(String(255))
    category = Column(String(255))
    instructors = Column(String(255))
    dates = Column(String(255))
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
        my_dict = self.__dict__
        del my_dict["_sa_instance_state"]
        return my_dict

    def dict_repr(self):
        return {
            "name": self.name,
            "teacher": self.instructors,
            "days and time": self.dates,
        }
