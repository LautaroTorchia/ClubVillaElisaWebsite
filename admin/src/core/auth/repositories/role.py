from src.core.auth.role import Role
from src.core.auth import roles

# adds permission to role
def add_permission_to_role(role, permission):
    """Add permission to role"""
    role.permissions.append(permission)
    roles.add(role)


# removes permission to role
def remove_permission_to_role(role, permission):
    """Add permission to role"""
    try:
        role.permissions.remove(permission)
        roles.add(role)
    except:
        pass


def create_role(role_name):
    role = Role(role_name)
    roles.add(role)
    return role


def get_roles():
    return roles.list()


def get_role(role_name):
    try:
        role = roles.filter("name", role_name)[0]
        return role
    except:
        return None
