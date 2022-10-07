from flask_wtf import FlaskForm
from wtforms import StringField, validators,PasswordField

class UserForm(FlaskForm):
    first_name = StringField('Nombre', validators=[validators.input_required()])
    last_name = StringField('Apellido', validators=[validators.input_required()])
    email = StringField('Email', validators=[validators.input_required()])
    username = StringField('Nombre de usuario', validators=[validators.input_required()])
    password = PasswordField('Contraseña', validators=[validators.input_required()])
    
class UpdateUserForm(FlaskForm):
    first_name = StringField('Nombre', validators=[validators.input_required()])
    last_name = StringField('Apellido', validators=[validators.input_required()])
    email = StringField('Email', validators=[validators.input_required()])
    username = StringField('Nombre de usuario', validators=[validators.input_required()])
