from core.auth import get_user_by_id
from wtforms.form import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, validators
from wtforms.validators import ValidationError

class UserForm(Form):
    first_name = StringField('Nombre', validators=[validators.input_required()])
    last_name = StringField('Apellido', validators=[validators.input_required()])
    email = StringField('Email', validators=[validators.input_required(), validators.Email()])
    username = StringField('Nombre de usuario', validators=[validators.input_required()])
    password = StringField('Contraseña', validators=[validators.input_required()])
    