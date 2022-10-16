from wtforms.validators import Length, InputRequired
from wtforms import StringField, PasswordField, EmailField, SelectMultipleField
from wtforms.widgets import CheckboxInput, ListWidget
from src.web.forms.base_form import BaseForm


class MultiCheckboxField(SelectMultipleField):
    """A multiple-select, except displays a list of checkboxes."""

    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class UserForm(BaseForm):
    """Form to create a new user
    first_name: First name of the user
    last_name: Last name of the user
    email: Email of the user
    username: Username of the user
    password: Password of the user
    roles: Roles of the user
    """    
    first_name = StringField("Nombre", validators=[Length(max=255), InputRequired()])
    last_name = StringField("Apellido", validators=[Length(max=255), InputRequired()])
    email = EmailField("Email", validators=[Length(max=255), InputRequired()])
    username = StringField(
        "Nombre de usuario", validators=[Length(max=255), InputRequired()]
    )
    password = PasswordField(
        "Contraseña", validators=[Length(max=255), InputRequired()]
    )
    roles = MultiCheckboxField("Roles", validate_choice=False, choices=[])

    def __init__(self, formdata=..., **kwargs):
        super().__init__(**kwargs)
        try:
            self["roles"].choices = kwargs["roles"]
        except:
            pass


class UpdateUserForm(BaseForm):
    """Form to update a user
    first_name: First name of the user
    last_name: Last name of the user
    email: Email of the user
    username: Username of the user
    roles: Roles of the user
    """   
    first_name = StringField("Nombre", validators=[Length(max=255), InputRequired()])
    last_name = StringField("Apellido", validators=[Length(max=255), InputRequired()])
    email = EmailField("Email", validators=[Length(max=255), InputRequired()])
    username = StringField(
        "Nombre de usuario", validators=[Length(max=255), InputRequired()]
    )
    roles = MultiCheckboxField("Roles", validate_choice=False, choices=[])

    def __init__(self, formdata=..., **kwargs):
        """Args:
            formdata (dict): Form data
        """        
        super().__init__(**kwargs)
        try:
            self["roles"].choices = kwargs["roles"]
        except:
            pass
