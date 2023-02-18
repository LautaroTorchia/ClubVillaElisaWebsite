from src.core.db import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean, default=False)

    def to_dict(self):
        my_dict = self.__dict__
        del my_dict["_sa_instance_state"]
        return my_dict
