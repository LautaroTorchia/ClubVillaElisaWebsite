from wtforms.validators import Length, InputRequired, Email, ValidationError
from wtforms import StringField, PasswordField, EmailField, SelectMultipleField
from wtforms.widgets import CheckboxInput, ListWidget
from src.web.forms.base_form import BaseForm
from src.core.auth.repositories.user import get_user_by_email


class MultiCheckboxField(SelectMultipleField):
    """A multiple-select, except displays a list of checkboxes."""

    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class BasicUserForm(BaseForm):
    first_name = StringField("Nombre", validators=[Length(max=255), InputRequired()])
    last_name = StringField("Apellido", validators=[Length(max=255), InputRequired()])
    email = EmailField("Email", validators=[Length(max=255), InputRequired(), Email()])
    username = StringField(
        "Nombre de usuario", validators=[Length(max=255), InputRequired()]
    )

    def validate_DNI_number(form, field):
        """Args:
            form (CreateAssociateForm): Form to create a new associate
            field (DNI_number): DNI number of the associate
        Raises:
            ValidationError: If the DNI number is already in use
        Returns:
            Boolean: True if the DNI number is not in use
        """
        if get_user_by_email(field.data):
            raise ValidationError("Email ya registrado")
        return True


class UserForm(BasicUserForm):
    """Form to create a new user
    first_name: First name of the user
    last_name: Last name of the user
    email: Email of the user
    username: Username of the user
    password: Password of the user
    roles: Roles of the user
    """

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


class UpdateUserForm(BasicUserForm):
    """Form to update a user
    first_name: First name of the user
    last_name: Last name of the user
    email: Email of the user
    username: Username of the user
    roles: Roles of the user
    """

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
