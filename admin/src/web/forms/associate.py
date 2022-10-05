from core.board import get_associate_by_DNI
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, validators
from wtforms.validators import ValidationError



class CreateAssociateForm(FlaskForm):
    
    name= StringField('Nombre', validators=[validators.DataRequired()])
    surname= StringField('Apellido', validators=[validators.DataRequired()])
    email= StringField('Email')
    DNI_number = IntegerField('DNI', validators=[validators.input_required()])
    DNI_type  = SelectField('Tipo de documento', choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE')],validators=[validators.input_required()])
    gender = SelectField('Genero', choices=[('male', 'Hombre'), ('female', 'Mujer'), ('other', 'Otro')],validators=[validators.input_required()])
    address = StringField('Direccion', validators=[validators.input_required()])
    phone_number = StringField('Telefono')
    
    
    def validate_DNI_number(form, field):
        print("validating DNI")
        print(get_associate_by_DNI(field.data))
        if get_associate_by_DNI(field.data):
            raise ValidationError('DNI ya registrado')
        return True


class UpdateAssociateForm(FlaskForm):
    
    name= StringField('Nombre', validators=[validators.DataRequired()])
    surname= StringField('Apellido', validators=[validators.DataRequired()])
    email= StringField('Email')
    gender = SelectField('Genero', choices=[('male', 'Hombre'), ('female', 'Mujer'), ('other', 'Otro')],validators=[validators.input_required()])
    address = StringField('Direccion', validators=[validators.input_required()])
    phone_number = StringField('Telefono')
    
