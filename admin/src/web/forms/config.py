from src.web.forms.base_form import BaseForm
from wtforms import StringField, validators, SelectField, DecimalField, IntegerField
from wtforms.validators import NumberRange


class ConfigForm(BaseForm):
    """Form to create a new config
    record_number: Amount of records to show in a page
    currency: Currency to use in the system
    base_fee: Base price of the club's fee
    due_fee: Percentage of the base fee to pay for expired payments
    payment_available: Visibility of the payments table on the public page
    contact: Contact info of the club
    payment_header: Header text of the payment receipts
    """

    record_number = IntegerField(
        "Cantidad de filas por página",
        default=5,
        validators=[
            validators.input_required(),
            NumberRange(min=1, message="No pueden haber 0 filas por página"),
        ],
    )
    currency = SelectField(
        "Moneda",
        choices=[("ARS", "Peso Argentino"), ("USD", "Dolar")],
    )
    base_fee = DecimalField(
        "Cuota mensual base",
        default=500,
        validators=[
            validators.input_required(),
            validators.number_range(min=0, message="El monto no puede ser negativo"),
        ],
    )
    due_fee = DecimalField(
        "Recargo por cuota adeudada (%)",
        default=10,
        validators=[
            validators.input_required(),
            NumberRange(
                0,
                100,
                message="El recargo por cuota adeudada debe estar entre 0 y 100.",
            ),
        ],
    )
    payment_available = SelectField(
        "Tabla de pago pública",
        choices=[("True", "Disponible"), ("False", "No disponible")],
    )
    contact = StringField(
        "Información de contacto",
        default="Ejemplo@gmail.com",
        validators=[validators.input_required()],
    )
    payment_header = StringField(
        "Encabezado de recibos de pago",
        default="Club Deportivo Villa Elisa",
        validators=[validators.input_required()],
    )
