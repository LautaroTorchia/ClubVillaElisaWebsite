from src.core.resource_manager import ResourceManager
from src.core.db import db
from src.core.board.associate import Associate, associate_disciplines
from src.core.board.discipline import Discipline
from src.core.board.payment import Payment

associates = ResourceManager(db.session, Associate)
disciplines = ResourceManager(db.session, Discipline)
payments = ResourceManager(db.session, Payment)


from src.core.board.repositories.configuration import *
from src.core.board.repositories.discipline import *
from src.core.board.repositories.associate import *
from src.core.board.repositories.payments import *
