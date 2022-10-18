from logging import PlaceHolder
from core.board import get_associate_by_DNI
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, validators,EmailField
from wtforms.validators import ValidationError



class CreateAssociateForm(FlaskForm):
    """Form to create a new associate
    name: Name of the associate
    surname: Surname of the associate
    email: Email of the associate
    DNI_number: DNI number of the associate
    DNI_type: DNI type of the associate
    gender: Gender of the associate
    address: Address of the associate
    phone_number: Phone of the associate
    """    
    
    name= StringField('Nombre', validators=[validators.DataRequired()])
    surname= StringField('Apellido', validators=[validators.DataRequired()])
    email= EmailField('Email')
    DNI_number = IntegerField('DNI', validators=[validators.input_required()])
    DNI_type  = SelectField('Tipo de documento', choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE')],validators=[validators.input_required()])
    gender = SelectField('Genero', choices=[('male', 'Hombre'), ('female', 'Mujer'), ('other', 'Otro')],validators=[validators.input_required()])
    address = StringField('Direccion', validators=[validators.input_required()])
    phone_number = StringField('Telefono')
    
    def validate_DNI_number(form, field):
        """Args:
            form (CreateAssociateForm): Form to create a new associate
            field (DNI_number): DNI number of the associate
        Raises:
            ValidationError: If the DNI number is already in use
        Returns:
            Boolean: True if the DNI number is not in use
        """        
        if get_associate_by_DNI(field.data):
            raise ValidationError('DNI ya registrado')
        return True


class UpdateAssociateForm(FlaskForm):
    """Form to update an associate
    name: Name of the associate
    surname: Surname of the associate
    email: Email of the associate
    gender: Gender of the associate
    address: Address of the associate
    phone_number: Phone of the associate
    active: Active status of the associate
    """  
    
    name= StringField('Nombre', validators=[validators.DataRequired()])
    surname= StringField('Apellido', validators=[validators.DataRequired()])
    email= EmailField('Email')
    gender = SelectField('Genero', choices=[('male', 'Hombre'), ('female', 'Mujer'), ('other', 'Otro')], validators=[validators.input_required()])
    address = StringField('Direccion', validators=[validators.input_required()])
    phone_number = StringField('Telefono')
    active = SelectField('Disponible',choices=[("True",'Activo'),("False",'Inactivo')],validators=[validators.input_required()])
    