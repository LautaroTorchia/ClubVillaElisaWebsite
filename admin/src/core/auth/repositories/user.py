from src.core.auth.user import User
from passlib.hash import sha256_crypt
from src.core.auth import users


def get_user_by(value, field="id"):
    """Args:
        user_id (int): The id of the user to retrieve.
    Returns:
        User: The user object.
    """
    return users.get(value, field)


def list_users(column=None, filter=True, paginate=True):
    """Args:
        column (int, optional): The column to order by. Defaults to None.
        filter (bool, optional): Whether to filter by active or not. Defaults to True.
    Returns:
        List: A paginated list of users.
    """
    if column:
        return users.filter(column, filter)
    return users.list(paginate=paginate)


def create_user(form):
    """Args:
        form (Form): The form to create the user from.
    Returns:
        User: The created user object.
    """
    user = User(**form)
    users.add(user)
    return user


def delete_user(user_id):
    """Args:
    user_id (int): The id of the user to delete.
    """
    user = get_user_by(value=user_id)
    for roles in user.roles:
        remove_role_to_user(user, roles)
    users.delete(user_id)


def update_user(user_id, form):
    """Args:
    user_id (int): The id of the user to update.
    form (Form): The form to update the user from.
    """
    users.update(user_id, form)


def get_by_usr_and_pwd(usr, pwd):
    """Args:
        usr (str): The name of the user to retrive.
        pwd (str): The password of the user to retrive.
    Returns:
        User: The user object.
    """
    usr = users.query.filter(User.username == usr).first()
    if usr != None and sha256_crypt.verify(pwd, usr.password):
        return usr
    return None


def get_by_email_and_pwd(email, pwd):
    """Args:
        email (str): The email of the user to retrive.
        pwd (str): The password of the user to retrive.
    Returns:
        User: The user object.
    """
    usr = users.query.filter(User.email == email).first()
    if usr != None and sha256_crypt.verify(pwd, usr.password):
        return usr
    return None


def disable_user(id):
    """Args:
    id (int): The id of the user to disable.
    """
    users.update(id, {"active": False})


def enable_user(id):
    """Args:
    id (int): The id of the user to enable.
    """
    users.update(id, {"active": True})


def add_role_to_user(user, role):
    """Args:
    user (User): The user to add the role to.
    role (Role): The role to add to the user.
    """
    user.roles.append(role)
    users.add(user)


def remove_role_to_user(user, role):
    """Args:
    user (User): The user to remove the role from.
    role (Role): The role to remove from the user.
    """
    try:
        user.roles.remove(role)
        users.add(user)
    except:
        pass


def user_has_permission(user_id, permission):
    """Args:
        user_id (int): The id of the user to check.
        permission (Permission): The permission to check.
    Returns:
        Boolean: Whether the user has the permission or not.
    """
    from src.core.auth import role_has_permission

    user = get_user_by(value=user_id)
    return any([role_has_permission(role, permission) for role in user.roles])
