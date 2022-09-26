from flask import render_template

def bad_request_error(e):
    """HTTP Error 400 (Bad Request)"""    
    kwargs = {
        "error_name": "400 Bad Request",
        "error_description": "Error en petición al servidor",
        }
    return render_template("error.html", **kwargs), 400

def unauthorized_error(e):
    """HTTP Error 401 (Unauthorized)"""    
    kwargs = {
        "error_name": "401 Access Unauthorized",
        "error_description": "El accesso no está autorizado",
        }
    return render_template("error.html", **kwargs), 401

def forbidden_error(e):
    """HTTP Error 403 (Forbidden)"""    
    kwargs = {
        "error_name": "403 Access Forbidden",
        "error_description": "El acceso al recurso fue prohibido",
        }
    return render_template("error.html", **kwargs), 403

def not_found_error(e):
    """HTTP Error 404 (Not Found)"""
    kwargs = {
        "error_name": "404 Page Not Found",
        "error_description": "No se encontro la URL",
        }
    return render_template("error.html", **kwargs), 404

def internal_server_error(e):
    """HTTP Error 500 (Internal Server Error)"""    
    kwargs = {
        "error_name": "500 Internal Server Error",
        "error_description": "Error interno del servidor. Inténtelo de nuevo más tarde",
        }
    return render_template("error.html", **kwargs), 500
