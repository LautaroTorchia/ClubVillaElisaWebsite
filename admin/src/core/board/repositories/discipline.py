from src.web.helpers.form_utils import bool_checker, csrf_remover
from src.core.board.discipline import Discipline
from src.core.board import disciplines
from src.core.board.repositories.associate import remove_discipline_to_associate


def list_disciplines(column=None, filter=True):
    """List all disciplines paginated with an option for a filter
    Returns:
        - List of Discipline objects
    """
    if column:
        return disciplines.filter(column, filter)
    return disciplines.list()


def list_all_disciplines(column=None, filter=True):
    """List all disciplines
    Returns:
        - List of Discipline objects
    """
    if column:
        return disciplines.filter(column, filter, paginate=False)
    return disciplines.list(paginate=False)


def get_last_discipline():
    """List last discipline
    Returns:
        - List of Discipline objects
    """
    return disciplines.query.order_by(Discipline.id.desc()).first()


def get_discipline(id):
    """Get discipline
    Returns:
        - Get discipline by id
    """
    return disciplines.get(id)


def delete_discipline(id):
    """Get discipline
    Returns:
        - Get discipline by id
    """
    for associate in disciplines.get(id).associates:
        remove_discipline_to_associate(associate, disciplines.get(id))
    disciplines.delete(id)


def update_discipline(id, discipline_data):
    """Get discipline
    Returns:
        - Get discipline by id
    """
    discipline_data = csrf_remover(discipline_data)
    discipline_data.update(available=bool_checker(discipline_data["available"]))
    disciplines.update(id, discipline_data)


def add_discipline(discipline_data, currency="ARS"):
    """Add discipline
    Returns:
        - Add discipline
    """
    discipline_data = csrf_remover(discipline_data)
    discipline_data.update(available=bool_checker(discipline_data["available"]))
    disciplines.add(Discipline(discipline_data))
