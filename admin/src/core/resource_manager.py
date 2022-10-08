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
