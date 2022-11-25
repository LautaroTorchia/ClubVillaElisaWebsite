import json
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
    paid_late = Column(Boolean(), default=False)
    amount = Column(Float)
    installment_number = Column(Integer)
    deleted = Column(Boolean(), default=False)

    associate_id = Column(Integer, db.ForeignKey("associates.id"), nullable=False)
    associate = db.relationship("Associate")

    def __init__(
        self, amount, installment_number, associate_id, date=None, paid_late=False
    ):
        self.amount = amount
        self.installment_number = installment_number
        self.associate_id = associate_id
        self.date = date
        self.paid_late = paid_late

    def __repr__(self):
        return f"""{self.date} fecha de pago de 
            la cuota {self.installment_number} con costo {self.amount}"""

    def to_dict(self):
        my_dict = self.__dict__
        my_dict["date"] = my_dict["date"].strftime("%Y-%m-%d %H:%M:%S.%f")
        del my_dict["_sa_instance_state"]
        return my_dict
