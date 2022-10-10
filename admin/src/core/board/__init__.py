from src.core.resource_manager import ResourceManager
from src.core.db import db
from src.core.board.associate import Associate
from src.core.board.discipline import Discipline

associates = ResourceManager(db.session, Associate)
disciplines = ResourceManager(db.session, Discipline)

#here is where CRUD are made
#QUESTION TO ASK TO GROUP, shall we do it in a CLASS or in different functions?

from src.core.board.repositories.configuration import *
from src.core.board.repositories.discipline import *
from src.core.board.repositories.associate import *