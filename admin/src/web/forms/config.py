from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, DecimalField, IntegerField

class ConfigForm(FlaskForm):
    record_number = IntegerField('Cantidad de filas por página', default=5, validators=[validators.input_required()])
    currency = SelectField('Moneda', choices=[('ARS', 'Peso Argentino'), ('USD', 'Dolar')], validators=[validators.input_required()])
    base_fee = DecimalField('Cuota mensual base', default=500, validators=[validators.input_required()])
    due_fee = IntegerField('Recargo por cuota adeudada (%)', default=10, validators=[validators.input_required()])
    payment_available = SelectField('Tabla de pago pública', choices=[(True, 'Disponible'), (False, 'No disponible')], validators=[validators.input_required()])
    contact = StringField('Información de contacto', default="Ejemplo@gmail.com", validators=[validators.input_required()])
    payment_header = StringField('Encabezado de recibos de pago', default="Club Deportivo Villa Elisa", validators=[validators.input_required()])
