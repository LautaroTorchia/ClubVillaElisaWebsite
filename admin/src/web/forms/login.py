from wtforms import StringField, PasswordField
from wtforms.validators import Length, InputRequired, NumberRange, Regexp
from src.web.forms.base_form import BaseForm

class LoginForm(BaseForm):
    """Form to login
    username: Username of the user
    password: Password of the user
    """    
    username = StringField('', validators=[Length(max=255), InputRequired()], render_kw={"placeholder": "Usuario"})
    password = PasswordField('', validators=[Length(max=255), InputRequired()], render_kw={"placeholder": "Contraseña"})
