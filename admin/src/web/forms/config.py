from wtform.form import Form
from wtform import StringField, validators, PasswordField

class ConfigForm(Form):
    cant_elems = StringField('Nombre', validators=[validators.input_required()])

