from flask_wtf import FlaskForm
from wtforms.validators import Length, InputRequired
from wtforms import StringField, PasswordField, EmailField, SelectMultipleField
from wtforms.widgets import CheckboxInput, ListWidget
from src.web.forms.base_form import BaseForm


class MultiCheckboxField(SelectMultipleField):
    """A multiple-select, except displays a list of checkboxes."""

    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class UserForm(BaseForm):
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
    first_name = StringField("Nombre", validators=[Length(max=255), InputRequired()])
    last_name = StringField("Apellido", validators=[Length(max=255), InputRequired()])
    email = EmailField("Email", validators=[Length(max=255), InputRequired()])
    username = StringField(
        "Nombre de usuario", validators=[Length(max=255), InputRequired()]
    )
    roles = MultiCheckboxField("Roles", validate_choice=False, choices=[])

    def __init__(self, formdata=..., **kwargs):
        super().__init__(**kwargs)
        try:
            self["roles"].choices = kwargs["roles"]
        except:
            pass
