from sqlalchemy import Float, DateTime, Integer, Column
from src.core.db import db


class Payment(db.Model):
    """Club payment Model
    Args:
        date (datetime): Payment date
        amount  (float): Amount of payment
        installment_number (int): Number of payment
    """

    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    amount = Column(Float)
    installment_number = Column(Integer)
    

    associate = db.relationship("Associate")
    associate_associate_number = Column(Integer, db.ForeignKey("associates.associate_number"), nullable=False)
    discipline = db.relationship("Discipline", back_populates="payments")
    discipline_id = Column(Integer, db.ForeignKey("disciplines.id"), nullable=False)

    def __init__(self, date, amount, installment_number):
        self.date = date
        self.amount = amount
        self.installment_number = installment_number

    def __repr__(self):
        return f"""{self.date} fecha de pago de 
            la cuota {self.installment_number} con costo {self.amount}"""
