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

    def __init__(self, name, category, instructors, dates, monthly_cost, available):
        self.name = name
        self.category = category
        self.instructors = instructors
        self.dates = dates
        self.monthly_cost = monthly_cost
        self.available = available

    def __repr__(self):
        return f"""{self.name} en la categoría {self.category} 
        con los instructores {self.instructors} 
        con un costo de {self.monthly_cost} y está disponible en los días y horaios{self.dates}"""
