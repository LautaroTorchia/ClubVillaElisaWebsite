from flask import render_template


def bad_request_error(e):
    """Args:
        e (Exception): Exception to be handled
    Returns:
        tuple: Redirects to the error page with the error description
    """
    kwargs = {
        "error_name": "400 Bad Request",
        "error_description": "Error en petición al servidor",
        "url_value": "home",
        "button_text": "Ir a la pagina principal",
    }
    return render_template("error.html", **kwargs), 400


def unauthorized_error(e):
    """Args:
        e (Exception): Exception to be handled
    Returns:
        tuple: Redirects to the error page with the error description
    """
    kwargs = {
        "error_name": "401 Access Unauthorized",
        "error_description": "El accesso no está autorizado",
        "url_value": "auth.login",
        "button_text": "Autenticarse",
    }
    return render_template("error.html", **kwargs), 401


def forbidden_error(e):
    """Args:
        e (Exception): Exception to be handled
    Returns:
        tuple: Redirects to the error page with the error description
    """
    kwargs = {
        "error_name": "403 Access Forbidden",
        "error_description": "El acceso al recurso fue prohibido",
        "url_value": "home",
        "button_text": "Ir a la pagina principal",
    }
    return render_template("error.html", **kwargs), 403


def not_found_error(e):
    """Args:
        e (Exception): Exception to be handled
    Returns:
        tuple: Redirects to the error page with the error description
    """
    kwargs = {
        "error_name": "404 Page Not Found",
        "error_description": "No se encontro la URL",
        "url_value": "home",
        "button_text": "Ir a la pagina principal",
    }
    return render_template("error.html", **kwargs), 404


def internal_server_error(e):
    """Args:
        e (Exception): Exception to be handled
    Returns:
        tuple: Redirects to the error page with the error description
    """
    kwargs = {
        "error_name": "500 Internal Server Error",
        "error_description": "Error interno del servidor. Inténtelo de nuevo más tarde",
        "url_value": "home",
        "button_text": "Ir a la pagina principal",
    }
    return render_template("error.html", **kwargs), 500
