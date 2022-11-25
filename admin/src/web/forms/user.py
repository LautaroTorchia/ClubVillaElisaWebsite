from wtforms.validators import Length, InputRequired, Email, ValidationError
from wtforms import StringField, PasswordField, EmailField, SelectMultipleField
from wtforms.widgets import CheckboxInput, ListWidget
from src.web.forms.base_form import BaseForm
from src.core.auth.repositories.user import get_user_by


class MultiCheckboxField(SelectMultipleField):
    """A multiple-select, except displays a list of checkboxes."""

    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class BasicUserForm(BaseForm):
    name = StringField("Nombre", validators=[Length(max=255), InputRequired()])
    surname = StringField("Apellido", validators=[Length(max=255), InputRequired()])
    email = EmailField("Email", validators=[Length(max=255), InputRequired(), Email()])
    username = StringField(
        "Nombre de usuario", validators=[Length(max=255), InputRequired()]
    )
    roles = MultiCheckboxField("Roles", validate_choice=False, choices=[])

    def __init__(self, formdata=..., **kwargs):
        self.user_id = kwargs.pop("user_id", None)
        super().__init__(**kwargs)
        try:
            self["roles"].choices = kwargs["roles"]
            if not self.user_id:
                self["roles"].choices = list(
                    filter(lambda x: x.name != "Socio", self["roles"].choices)
                )
            else:
                r = get_user_by(self.user_id).roles
                is_associate = list(filter(lambda x: x.name == "Socio", r))
                if is_associate == []:
                    self["roles"].choices = list(
                        filter(lambda x: x.name != "Socio", self["roles"].choices)
                    )
                else:
                    self["roles"].choices = is_associate

        except:
            pass

    def validate_email(self, field):
        """Args:
            form (CreateAssociateForm): Form to create a new associate
            field (DNI_number): DNI number of the associate
        Raises:
            ValidationError: If the DNI number is already in use
        Returns:
            Boolean: True if the DNI number is not in use
        """
        if self.user_id:
            if get_user_by(self.user_id).email != field.data and get_user_by(
                field.data, "email"
            ):
                raise ValidationError("Email ya registrado")
        else:
            if get_user_by(field.data, "email"):
                raise ValidationError("Email ya registrado")

        return True

    def validate_username(self, field):
        """Args:
            form (CreateAssociateForm): Form to create a new associate
            field (DNI_number): DNI number of the associate
        Raises:
            ValidationError: If the DNI number is already in use
        Returns:
            Boolean: True if the DNI number is not in use
        """
        if self.user_id:
            if get_user_by(self.user_id).username != field.data:
                raise ValidationError("No se puede cambiar el nombre de usuario")
        else:
            if get_user_by(field.data, "username"):
                raise ValidationError("Nombre de usuario ya registrado")
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
