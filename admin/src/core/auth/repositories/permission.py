from src.core.auth.permission import Permission
from src.core.auth import permissions


def create_permission(permission_name):
    permission = Permission(permission_name)
    permissions.add(permission)
    return permission


def get_permission(permission_name):
    try:
        permission = permissions.filter("name", permission_name)[0]
        return permission
    except:
        return None
