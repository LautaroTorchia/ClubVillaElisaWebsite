from wtforms.validators import Regexp
from flask_wtf import FlaskForm

class BaseForm(FlaskForm):
    alphabetic_validator = Regexp(regex='^[a-zA-ZñÑ ]+$', message='El nombre solo puede contener letras y espacios')
    class Meta:
        locales = ('es_ES', 'es')