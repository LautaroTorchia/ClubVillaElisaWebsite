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

    associates = db.relationship("Associate", secondary="associate_disciplines", back_populates="disciplines")

    def __init__(self, discipline_data):
        self.name=discipline_data["name"]
        self.category=discipline_data["category"]
        self.instructors=discipline_data["instructors"]
        self.dates=discipline_data["dates"]
        self.monthly_cost=discipline_data["monthly_cost"]
        self.available=bool_checker(discipline_data["available"])

    def __repr__(self):
        return f"""{self.name} en la categoría {self.category} 
        con los instructores {self.instructors} 
        con un costo de {self.monthly_cost} y está disponible en los días y horaios{self.dates}"""

    def to_dict(self):
        my_dict = self.__dict__
        del my_dict['_sa_instance_state']
        return my_dict

def bool_checker(attribute):
    if type(attribute) == bool:
        return attribute
    if type(attribute) == str:
        return True if attribute == "True" else False
    raise ValueError("This should be a bool or the str values 'True' o 'False'")