from src.core.auth import create_user,get_by_usr_and_pwd
from passlib.hash import sha256_crypt
def run():
    if(get_by_usr_and_pwd("admin","1234") is None):
        create_user({'first_name': 'admin', 'last_name': 'admin', 'email': 'admin', 'username': 'admin', 'password': sha256_crypt.encrypt("1234")})
