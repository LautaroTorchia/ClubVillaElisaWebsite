from wtforms.validators import Regexp
from flask_wtf import FlaskForm


class BaseForm(FlaskForm):
    """FlaskForm (Form): Form to create a new associate"""

    alphabetic_validator = Regexp(
        regex="^(?:[^\W\d_]|[ ])+$",
        message="El nombre solo puede contener letras y espacios",
    )

    class Meta:
        locales = ("es_ES", "es")
