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
    return roles.list()


def get_role(role_name):
    """Args:
        role_name (str): The name of the role to retrieve.
    Returns:
        Role: The role object.
    """    
    try:
        role = roles.filter("name", role_name)[0]
        return role
    except:
        return None
