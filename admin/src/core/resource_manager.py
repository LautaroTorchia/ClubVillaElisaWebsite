from typing import Union
from sqlalchemy.sql.expression import cast
from sqlalchemy import String
from sqlalchemy.sql.expression import ColumnOperators
from flask_sqlalchemy import Pagination
from sqlalchemy import Table


class ResourceManager:

    model_class = None

    def __init__(self, dbsession, model_class):
        """Args:
        dbsession (SQLAlchemy Session): The SQLAlchemy session.
        model_class (SQLAlchemy Model): The SQLAlchemy model.
        """
        self.dbs = dbsession
        self.model_class = model_class

    def _base_query(self, model):
        """Returns:
        SQLAlchemy Query: The SQLAlchemy query.
        """
        return self.dbs.query(model).filter(model.deleted == False)

    @property
    def query(self):
        """Returns:
        SQLAlchemy Query: The SQLAlchemy query.
        """
        return self._base_query(self.model_class)

    def add(self, obj):
        """Args:
        obj (Object): The object to add.
        """
        try:
            self.dbs.add(obj)
            self.dbs.commit()
        except Exception as e:
            self.dbs.rollback()
            raise e

    def _base_filter(self, col_name, text, query_in=None, class_in=None):
        """Args:
            col_name (String): The column name.
            text (String): The text to filter.
        Returns:
            SQLAlchemy Query: The SQLAlchemy query.
        """
        if query_in:
            return query_in.filter(
                cast(getattr(class_in, col_name), String).ilike(f"%{text}%")
            )
        return self.query.filter(
            cast(getattr(self.model_class, col_name), String).ilike(f"%{text}%")
        )

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

    def get(self, value, field="id"):
        """Args:
            field (String): The field to filter.
            value (Any): The value to filter.
        Returns:
            Object: First object of list.
        """
        return self.query.filter(getattr(self.model_class, field) == value).first()

    def list(
        self, order_criteria: ColumnOperators = None, paginate: bool = True
    ) -> Union[Pagination, list]:
        """Returns a list of objects. pagination is enabled by default. order_criteria is optional.

        Args:
            order_criteria (ColumnOperators, optional): The order of the records . Defaults to None.
            paginate (bool, optional): Paginate if true, record_amount comes from config. Defaults to True.

        Returns:
            Union[Pagination, list]: if pagination is enabled returns a Pagination object, otherwise a list.
        """
        from src.core.board.repositories.configuration import get_cfg

        ordered_query = self.query.order_by(order_criteria)
        if paginate:
            return ordered_query.paginate(
                per_page=get_cfg().record_number, error_out=False
            )
        return ordered_query.all()

    def filter(
        self,
        col_name: str,
        match: str,
        order_criteria: ColumnOperators = None,
        paginate: bool = True,
    ) -> Union[Pagination, list]:
        """Returns a list of filtered objects of a certain column. pagination is enabled by default. order_criteria is optional.

        Args:
            col_name (str): The column to apply the filter to
            match (str): The string to be matched, matches are by like
            order_criteria (ColumnOperators, optional): The order of the records . Defaults to None.
            paginate (bool, optional): Paginate if true, record_amount comes from config. Defaults to True.

        Returns:
            Union[Pagination, list]: if pagination is enabled returns a Pagination object, otherwise a list.
        """
        from src.core.board.repositories.configuration import get_cfg

        ordered_query = self._base_filter(col_name, match).order_by(order_criteria)
        if paginate:
            return ordered_query.paginate(
                per_page=get_cfg().record_number, error_out=False
            )
        return ordered_query.all()

    def _base_join(self, join_table):
        return (
            self._base_query(self.model_class)
            .join(join_table)
            .filter(join_table.deleted == False)
        )

    def join_search(
        self,
        col_name: str,
        match: str,
        join_table: Table,
        paginate: bool = True,
        order_criteria=False,
    ) -> Union[Pagination, list]:
        """Returns a list of filtered objects of a certain column of a join. pagination is enabled by default.

        Args:
            col_name (str): The column to apply the filter to
            match (str): The string to be matched, matches are by like
            join_table (Table): Table to join to the main table
            paginate (bool, optional): Paginate if true, record_amount comes from config. Defaults to True.

        Returns:
            Union[Pagination, list]: if pagination is enabled returns a Pagination object, otherwise a list.
        """

        from src.core.board.repositories.configuration import get_cfg

        ordered_query = self._base_filter(
            col_name, match, self._base_join(join_table), join_table
        ).order_by(order_criteria)
        if paginate:
            return ordered_query.paginate(
                per_page=get_cfg().record_number, error_out=False
            )
        return ordered_query.all()
