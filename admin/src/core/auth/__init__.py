from src.core.db import db
from src.core.resource_manager import ResourceManager
from src.core.auth.user import User

users = ResourceManager(db.session, User)

from src.core.auth.repositories.user import *