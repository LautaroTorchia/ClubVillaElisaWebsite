from src.web.helpers.build_response import response
from src.core.auth import get_by_usr_and_pwd, get_user_by
from flask import Blueprint, request, jsonify
from src.web.config import Config
from functools import wraps
from src.core.board import get_associate_by_DNI
import jwt

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    jwt_required,
    unset_jwt_cookies,
    get_jwt_identity,
)

auth_api_blueprint = Blueprint("auth_api", __name__, url_prefix="/auth")


@auth_api_blueprint.post("/login")
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    user = get_by_usr_and_pwd(username, password)

    try:
        if user and get_associate_by_DNI(user.username):
            token = create_access_token(identity=user.id)
            refresh = create_refresh_token(identity=user.id)
            res = jsonify()
            set_access_cookies(res, token)
            set_refresh_cookies(res, refresh)
            return res, 201
    except:
        return "Invalid credentials", 401
    return "Not found", 404


@auth_api_blueprint.post("/logout")
@jwt_required()
def logout():
    res = jsonify()
    unset_jwt_cookies(res)
    return res


@auth_api_blueprint.get("/user_jwt")
@jwt_required()
def user_jwt():
    current_user = get_jwt_identity()
    user = get_user_by(current_user)
    response = jsonify(user.to_dict())
    return response


@auth_api_blueprint.post("/refresh")
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    token = create_access_token(identity=current_user)
    res = jsonify()
    set_access_cookies(res, token)
    return res, 201
