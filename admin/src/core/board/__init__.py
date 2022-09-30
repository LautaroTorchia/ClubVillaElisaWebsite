#here is where CRUD are made
#QUESTION TO ASK TO GROUP, shall we do it in a CLASS or in different functions?
from dis import dis
from this import d
from src.core.board.associate import Associate
from src.core.board.discipline import Discipline
from src.core.db import db

def get_associate_by_id(associate_number):
    """ Get associate by id
    Args:
        - associate_number (integer): Associate number. Unique, autogenerated
    Returns:
        - Associate object
    """
    return Associate.query.get(associate_number)

def get_associate_by_DNI(DNI_number):
    """ Get associate by DNI
    Args:
        - DNI_number (integer): Associate DNI number
    Returns:
        - Associate object
    """
    return Associate.query.filter_by(DNI_number=DNI_number).first()

def list_associates():
    """ List all associates
    Returns:
        - List of Associate objects
    """
    return Associate.query.all()

def create_associate(form):
    """ Create associate
    Returns:
        - Create associate
    """
    associate = Associate(**form.data)
    db.session.add(associate)
    db.session.commit()
    return associate

def list_disciplines():
    """ List all disciplines
    Returns:
        - List of Discipline objects
    """
    return Discipline.query.all()

def get_discipline(id):
    """ Get discipline
    Returns:
        - Get discipline by id
    """
    return Discipline.query.get(id)

def delete_discipline(id):
    """ Get discipline
    Returns:
        - Get discipline by id
    """
    db.session.query(Discipline).filter(Discipline.id == id).delete()
    db.session.commit()

def update_discipline(id,discipline_data):
    """ Get discipline
    Returns:
        - Get discipline by id
    """
    db.session.query(Discipline).filter(Discipline.id == id).update(discipline_data)
    db.session.commit()


def add_discipline(discipline_data):
    """ Add discipline
    Returns:
        - Add discipline
    """
    db.session.add(discipline_data )
    db.session.commit()