from wtforms import StringField, DecimalField, SelectField, Label
from wtforms.validators import Length, InputRequired, NumberRange, Regexp
from src.web.forms.base_form import BaseForm

instructor_validator = Regexp(
    regex="^(?:[^\W\d_]|[ ,])+$",
    message="El nombre de un instructor solo puede contener letras y numeros, por favor separe los nombres de varios instructores con una coma",
)


class DisciplineForm(BaseForm):
    """Form to create a new discipline
    name: Name of the discipline
    category: Category of the discipline
    instructors: Name of the instructors
    dates: Dates and hours of the discipline
    monthly_cost: Monthly cost of the discipline
    available: Current availability of the discipline
    """

    name = StringField(
        "Nombre",
        validators=[BaseForm.alphabetic_validator, Length(max=255), InputRequired()],
    )
    category = StringField("Categoría", validators=[Length(max=255), InputRequired()])
    instructors = StringField(
        "Instructores",
        validators=[Length(max=255), InputRequired(), instructor_validator],
        description="Separe los nombres de los instructores con una coma",
    )
    dates = StringField(
        "Días y horarios", validators=[Length(max=255), InputRequired()]
    )
    monthly_cost = DecimalField(
        "Costo mensual",
        validators=[
            InputRequired(),
            NumberRange(0, message="El costo mensual debe ser mayor a 0"),
        ],
    )
    available = SelectField(
        "Disponible", choices=[(True, "Disponible"), ("False", "No disponible")]
    )
