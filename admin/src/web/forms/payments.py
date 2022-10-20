from wtforms import StringField, DecimalField, SelectField, Label, IntegerField
from wtforms.validators import Length, InputRequired, NumberRange, Regexp
from src.web.forms.base_form import BaseForm

instructor_validator = Regexp(
    regex="^(?:[^\W\d_]|[ ,])+$",
    message="El nombre de un instructor solo puede contener letras y numeros, por favor separe los nombres de varios instructores con una coma",
)


class PaymentUpdateForm(BaseForm):
    """Form to update a new payment
    name: Name of the associate
    surname: Surname of the associate
    date: payment date
    amount: payment amount
    """

    # payment fields
    name = StringField("Nombre", validators=[Length(max=50)])
    surname = StringField("Apellido", validators=[Length(max=50)])
    date = StringField("Fecha", validators=[Length(max=50)])
    paid_late = StringField("Pago fuera de termino")
    installment_number = IntegerField("Numero de Cuota")
    tipo_de_moneda = StringField("Tipo de moneda")
    amount = IntegerField("Monto", validators=[NumberRange(min=0, max=10000000000)])
