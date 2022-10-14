from src.core.db import db
from src.core.resource_manager import ResourceManager
from src.core.auth.user import User
from src.core.auth.role import Role
from src.core.auth.permission import Permission

roles = ResourceManager(db.session, Role)
users = ResourceManager(db.session, User)
permissions = ResourceManager(db.session, Permission)

from src.core.auth.repositories.user import *
from src.core.auth.repositories.role import *
from src.core.auth.repositories.permission import *
