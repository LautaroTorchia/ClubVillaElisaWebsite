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
    """Returns:
        List: List of all permissions
    """      
    modules_operator = ["associate", "discipline","payments"]
    modules_admin = [*modules_operator, "user", "configuration"]
    actions_operator = ["index", "show", "update", "create"]
    actions_admin = [*actions_operator, "destroy"]

    operator_permissions = [
        "associate_add_discip",
        "associate_remove_discip",
        "payments_import",
    ]
    
    admin_permissions = [*operator_permissions, "payments_destroy"]

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
