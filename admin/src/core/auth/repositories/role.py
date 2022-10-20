from src.core.auth.role import Role
from src.core.auth import roles

# adds permission to role
def add_permission_to_role(role, permission):
    """Args:
    role (Role): The role to add the permission to.
    permission (Permission): The permission to add to the role.
    """
    role.permissions.append(permission)
    roles.add(role)


# removes permission to role
def remove_permission_to_role(role, permission):
    """Args:
    role (Role): The role to remove the permission from.
    permission (Permission): The permission to remove from the role.
    """
    try:
        role.permissions.remove(permission)
        roles.add(role)
    except:
        pass


def create_role(role_name):
    """Args:
        role_name (str): The name of the role to create.
    Returns:
        Role: The created role object.
    """
    role = Role(role_name)
    roles.add(role)
    return role


def get_roles():
    """Returns:
    List: A list of all roles.
    """
    return roles.list(paginate=False)


def get_role(role_name):
    """Args:
        role_name (str): The name of the role to retrieve.
    Returns:
        Role: The role object.
    """
    try:
        return roles.filter("name", role_name, paginate=False)[0]
    except:
        return None


def role_has_permission(role, permission):
    """Args:
        role (Role): The role to check.
        permission (Permission): The permission to check.
    Returns:
        bool: True if the role has the permission, False otherwise.
    """
    return permission in map(lambda perm: perm.name, role.permissions)
