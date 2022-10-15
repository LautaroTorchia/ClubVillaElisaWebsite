from functools import wraps
from flask import session, abort
from src.core.auth import user_has_permission


def is_authenticated(session):
    return session.get("user") != None


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return abort(401)
        return f(*args, **kwargs)

    return decorated_function


def get_permissions():
    modules_operator = ["associate", "discipline"]
    modules_admin = [*modules_operator, "user", "configuration"]
    actions_operator = ["index", "show", "update", "create"]
    actions_admin = [*actions_operator, "destroy"]

    operator_permissions = [
        "associate_add_discip",
        "associate_remove_discip",
        "payment_index",
        "payment_show",
        "payment_import",
    ]
    admin_permissions = [*operator_permissions, "payment_destroy"]

    for mod in modules_operator:
        for act in actions_operator:
            operator_permissions.append(f"{mod}_{act}")

    for mod in modules_admin:
        for act in actions_admin:
            admin_permissions.append(f"{mod}_{act}")

    return operator_permissions, admin_permissions


def check_permission(user_id, permission):
    return user_has_permission(user_id, permission)


def has_permission(permission):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if session.get("user") is None:
                return abort(401)
            if not check_permission(session.get("user"), permission):
                return abort(403)
            return f(*args, **kwargs)

        return wrapper

    return decorator
