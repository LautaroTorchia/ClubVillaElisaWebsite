from sqlalchemy import Float, DateTime, Integer, Column, Boolean
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
    date = Column(db.DateTime, default=db.func.now())
    amount = Column(Float)
    installment_number = Column(Integer)
    deleted = Column(Boolean(), default=False)
    
    
    associate_id = Column(Integer, db.ForeignKey("associates.id"), nullable=False)
    associate = db.relationship("Associate")

    def __init__(self, amount, installment_number):
        self.amount = amount
        self.installment_number = installment_number

    def __repr__(self):
        return f"""{self.date} fecha de pago de 
            la cuota {self.installment_number} con costo {self.amount}"""
