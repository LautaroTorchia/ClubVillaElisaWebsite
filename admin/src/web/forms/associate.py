from core.board import get_associate_by_DNI
from wtforms.form import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField,validators
from wtforms.validators import ValidationError



class AssociateForm(Form):
    
    name= StringField('Nombre', validators=[validators.DataRequired()])
    surname= StringField('Apellido', validators=[validators.DataRequired()])
    email= StringField('Email')
    DNI_number = IntegerField('DNI', validators=[validators.input_required()])
    DNI_type  = SelectField('Tipo de documento', choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE')],validators=[validators.input_required()])
    gender = SelectField('Genero', choices=[('male', 'Hombre'), ('female', 'Mujer'), ('other', 'Otro')],validators=[validators.input_required()])
    address = StringField('Direccion', validators=[validators.input_required()])
    phone_number = StringField('Telefono')
    add_associate= SubmitField('Agregar Asociado')
    
    
    def validate_DNI_number(form, field):
        try:
            get_associate_by_DNI(field.data)
            raise ValidationError('DNI ya registrado')
        except:
            return True
