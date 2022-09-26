from flask import render_template

def not_found_error(e):
    kwargs = {
        "error_name": "404 Page Not Found",
        "error_description": "No se encontro la URL",
        }
    return render_template("error.html", **kwargs), 404
