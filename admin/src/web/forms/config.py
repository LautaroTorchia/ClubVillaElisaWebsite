from tabnanny import check
from tokenize import Number, String
from wtform.form import Form
from wtform import StringField, validators, SelectField, DecimalField

class ConfigForm(Form):
    record_number = StringField('Numero de registro', validators=[validators.input_required()])
    currency = SelectField('Moneda', choices=[('USD', 'Dolar'), ('EUR', 'Euro'), ('GBP', 'Libra'), ('ARS', 'Peso Argentino')], validators=[validators.input_required()])
    base_fee = DecimalField('Tarifa base', validators=[validators.input_required()])
    due_fee = DecimalField('Tarifa de vencimiento', validators=[validators.input_required()])
    payment_available = SelectField('Tabla de pago pública', choices=[(True, 'Disponible'), (False, 'No disponible')], validators=[validators.input_required()])
    contact = StringField('Información de contacto', validators=[validators.input_required()])
    payment_header = StringField('Encabezado de recibos de pago', validators=[validators.input_required()])
