import email
from core.auth import get_user_by_id
from wtforms.form import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, validators
from wtforms.validators import ValidationError

class UserForm(Form):
    firstName = StringField('Nombre', validators=[validators.input_required()])
    lastName = StringField('Apellido', validators=[validators.input_required()])
    email_adress = StringField('Email', validators=[validators.input_required()])
    username = StringField('Nombre de usuario', validators=[validators.input_required()])
    password = StringField('Contraseña', validators=[validators.input_required()])
    add_user = SubmitField('Agregar Usuario')
    