from flask_wtf import FlaskForm
from wtforms.validators import Length, InputRequired
from wtforms import StringField, PasswordField, EmailField

class UserForm(FlaskForm):
    first_name = StringField('Nombre', validators=[Length(max=255),InputRequired()])
    last_name = StringField('Apellido', validators=[Length(max=255),InputRequired()])
    email = EmailField('Email', validators=[Length(max=255),InputRequired()])
    username = StringField('Nombre de usuario', validators=[Length(max=255),InputRequired()])
    password = PasswordField('Contraseña', validators=[Length(max=255),InputRequired()])
    
class UpdateUserForm(FlaskForm):
    first_name = StringField('Nombre', validators=[Length(max=255),InputRequired()])
    last_name = StringField('Apellido', validators=[Length(max=255),InputRequired()])
    email = EmailField('Email', validators=[Length(max=255),InputRequired()])
    username = StringField('Nombre de usuario', validators=[Length(max=255),InputRequired()])
