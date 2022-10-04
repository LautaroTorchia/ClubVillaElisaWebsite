from sqlalchemy import Boolean, Column, String, Integer, Numeric
from src.core.db import db


class Configuration(db.Model):
    """Modelo de configuracion
    Args:
        record_number (int): How many records to show
        ord_criteria (str): How the data will be sorted
        currency (str): Currency type
        base_fee (float): Base fee used to calculate club fee
        due_fee (float): Fee due to payment delayed
        payment_available (bool): Toggle payment table in public app
        contact (str): Contact info
        payment_header (str): Information shown at payment receipt
    """

    __tablename__ = "configuration"
    id = Column(Integer, primary_key=True)
    record_number = Column(Integer)
    ord_criteria = Column(String(255))
    currency = Column(String(255))
    base_fee = Column(Numeric())
    due_fee = Column(Numeric())
    payment_available = Column(Boolean())
    contact = Column(String(255))
    payment_header = Column(String(255))

    def __init__(self, configuration_data):
        self.record_number = configuration_data["record_number"]
        self.ord_criteria = configuration_data["ord_criteria"]
        self.currency = configuration_data["currency"]
        self.base_fee=configuration_data["base_fee"]
        self.due_fee=configuration_data["due_fee"]
        self.payment_available=configuration_data["payment_available"]
        self.contact=configuration_data["contact"]
        self.payment_header=configuration_data["payment_header"]

    def __repr__(self):
        return f"""{self.record_number} elementos en orden {self.ord_criteria}, Moneda: {self.currency}"""

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
