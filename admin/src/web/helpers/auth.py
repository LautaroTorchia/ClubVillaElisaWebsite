from src.core.auth import user_has_permission, get_user_by
from src.web.helpers.build_response import response
from flask import session, abort, redirect, url_for
from flask import request, jsonify
from src.web.config import Config
from functools import wraps
import jwt


def is_authenticated(session):
    return session.get("user") != None


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return abort(401)
        return f(*args, **kwargs)

    return decorated_function


def check_logged(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is not None:
            return redirect(url_for("home"))

        return f(*args, **kwargs)

    return decorated_function


def get_permissions():
    """Returns:
    List: List of all permissions
    """
    modules_operator = ["associate", "discipline", "payments"]
    modules_admin = [*modules_operator, "user", "configuration"]
    actions_operator = ["index", "show", "update", "create"]
    actions_admin = [*actions_operator, "destroy"]

    operator_permissions = [
        "payments_import",
    ]

    admin_permissions = [*operator_permissions]

    for mod in modules_operator:
        for act in actions_operator:
            operator_permissions.append(f"{mod}_{act}")

    for mod in modules_admin:
        for act in actions_admin:
            admin_permissions.append(f"{mod}_{act}")

    return operator_permissions, admin_permissions


def check_permission(user_id, permission):
    """Args:
        user_id (int): Id of the user
        permission (str): Permission to check
    Returns:
        bool: True if the user has the permission, False otherwise
    """
    return user_has_permission(user_id, permission)


def has_permission(permission):
    """Args:
    permission (str): Permission to check
    """

    def decorator(f):
        """Args:
            f (function): Function to decorate
        Returns:
            function: Decorated function
        """

        @wraps(f)
        def wrapper(*args, **kwargs):
            """Returns:
            function: Decorated function
            """
            if session.get("user") is None:
                return abort(401)
            if not check_permission(session.get("user"), permission):
                return abort(403)
            return f(*args, **kwargs)

        return wrapper

    return decorator


def _jwt_required():
    """Does the actual work of verifying the JWT data in the current request.
    This is done automatically for you by `jwt_required()` but you could call it manually.
    Doing so would be useful in the context of optional JWT access in your APIs.

    """

    token = request.headers.get("Authorization", None)
    if token is None:
        abort(jsonify(response(400, "No token provided", "reason")))
    try:
        payload = jwt.decode(
            token.split(" ")[1], Config.SECRET_KEY, algorithms=["HS256"]
        )
    except jwt.InvalidTokenError:
        abort(jsonify(response(400, "Invalid token", "reason")))
    except IndexError:
        abort(jsonify(response(400, "Invalid token", "reason")))
    user = get_user_by(payload["id"])

    if user is None:
        abort(jsonify(response(401, "User not found", "reason")))
    return user


def jwt_required(fn):
    """View decorator that requires a valid JWT token to be present in the request"""

    @wraps(fn)
    def decorator(*args, **kwargs):
        user = _jwt_required()
        return fn(user)

    return decorator
