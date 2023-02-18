from sqlalchemy import Boolean, Column, String, Integer, Numeric
from src.core.db import db


class Configuration(db.Model):
    """Modelo de configuracion
    Args:
        record_number (int): How many records to show
        currency (str): Currency type
        base_fee (float): Base fee used to calculate club fee
        due_fee (int): Fee due % to payment delayed
        payment_available (bool): Toggle payment table in public app
        contact (str): Contact info
        payment_header (str): Information shown at payment receipt
    """

    __tablename__ = "configuration"
    id = Column(Integer, primary_key=True)
    record_number = Column(Integer)
    currency = Column(String())
    base_fee = Column(Numeric())
    due_fee = Column(Numeric())
    payment_available = Column(Boolean())
    contact = Column(String())
    payment_header = Column(String())

    def __init__(self, configuration_data):
        self.record_number = configuration_data["record_number"]
        self.currency = configuration_data["currency"]
        self.base_fee = configuration_data["base_fee"]
        self.due_fee = configuration_data["due_fee"]
        self.payment_available = configuration_data["payment_available"]
        self.contact = configuration_data["contact"]
        self.payment_header = configuration_data["payment_header"]

    def __repr__(self):
        return (
            f"""{self.record_number} cantidad de registros, moneda: {self.currency}"""
        )

    def to_dict(self):
        return {
            "id": self.id,
            "record_number": self.record_number,
            "currency": self.currency,
            "base_fee": self.base_fee,
            "due_fee": self.due_fee,
            "payment_available": self.payment_available,
            "contact": self.contact,
            "payment_header": self.payment_header,
        }
