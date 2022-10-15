from sqlalchemy.sql.expression import cast
from sqlalchemy import String


class ResourceManager():

    model_class = None

    def __init__(self, dbsession,model_class):
        """Args:
            dbsession (SQLAlchemy Session): The SQLAlchemy session.
            model_class (SQLAlchemy Model): The SQLAlchemy model.
        """        
        self.dbs = dbsession 
        self.model_class = model_class

    @property
    def query(self):
        """Returns:
            SQLAlchemy Query: The SQLAlchemy query.
        """        
        return self.dbs.query(self.model_class).filter(self.model_class.deleted==False)

    def add(self, obj):
        """Args:
            obj (Object): The object to add.
        """        
        self.dbs.add(obj)
        self.dbs.commit()

    def base_filter(self, col_name, text):
        """Args:
            col_name (String): The column name.
            text (String): The text to filter.
        Returns:
            SQLAlchemy Query: The SQLAlchemy query.
        """        
        return self.query.filter(
            cast(getattr(self.model_class, col_name), String).ilike(f"%{text}%")
        )

    def filter(self, col_name, text):
        """Args:
            col_name (String): The column name.
            text (String): The text to filter.
        Returns:
            _type_: The SQLAlchemy query.
        """        
        return self.base_filter(col_name, text).all()

    def update(self, id, data):
        """Args:
            id (Integer): The id of the object to update.
            data (Dictionary): The data to update.
        """        
        self.query.filter(self.model_class.id == id).update(data)
        self.dbs.commit()

    def delete(self, id):
        """Args:
            id (Integer): The id of the object to delete.
        """        
        self.query.filter(self.model_class.id == id).update({"deleted": True})
        self.dbs.commit()

    def get(self, id):
        """Args:
            id (Integer): The id of the object to get.
        Returns:
            Object: The object.
        """        
        return self.query.filter(self.model_class.id == id).first()

    def list(self):
        """Returns:
            List: The list of objects.
        """        
        return self.query.all()

    def paginated_list(self):
        """Returns:
            List: The paginated list of objects.
        """        
        from src.core.board.repositories.configuration import get_cfg
        return self.query.paginate(per_page=get_cfg().record_number, error_out=False)

    def paginated_filter(self, col_name, text):
        """Args:
            col_name (String): The column name.
            text (String): The text to filter.
        Returns:
            List: The paginated and filtered list of objects.
        """        
        from src.core.board.repositories.configuration import get_cfg
        return self.base_filter(col_name, text).paginate(per_page=get_cfg().record_number, error_out=False)

    def paginated_ordered_filter(self, col_name, text,order_criteria):
        """Args:
            col_name (String): The column name.
            text (String): The text to filter.
            order_criteria (String): The order criteria.
        Returns:
            List: The paginated, filtered and ordered list of objects.
        """        
        from src.core.board.repositories.configuration import get_cfg
        return self.base_filter(col_name, text).order_by(order_criteria).paginate(per_page=get_cfg().record_number, error_out=False)

    def paginated_ordered_list(self,order_criteria):
        """Args:
            order_criteria (String): The order criteria.
        Returns:
            List: The paginated and ordered list of objects.
        """        
        from src.core.board.repositories.configuration import get_cfg
        return self.query.order_by(order_criteria).paginate(per_page=get_cfg().record_number, error_out=False)
    