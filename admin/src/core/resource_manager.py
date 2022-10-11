from sqlalchemy.sql.expression import cast
from sqlalchemy import String

class ResourceManager():
    model_class = None

    def __init__(self, dbsession,model_class):
         self.dbs = dbsession 
         self.model_class = model_class

    @property
    def query(self):
         return self.dbs.query(self.model_class).filter(self.model_class.deleted==False)

    def add(self, obj):
        self.dbs.add(obj)
        self.dbs.commit()

    def filter(self, col_name, text):
        return self.query.filter(
            cast(getattr(self.model_class, col_name), String).like(f"%{text}%")
        ).all()

    def update(self, id, data):
        self.query.filter(self.model_class.id == id).update(data)
        self.dbs.commit()

    def delete(self, id):
        self.query.filter(self.model_class.id == id).update({"deleted": True})
        self.dbs.commit()

    def get(self, id):
        return self.query.filter(self.model_class.id == id).first()

    def list(self):
        return self.query.all()