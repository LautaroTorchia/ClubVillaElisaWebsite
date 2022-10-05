from wtforms import StringField, DecimalField,validators, SelectField
from wtforms.validators import Length, InputRequired
from flask_wtf import FlaskForm

alphabetic_validator = validators.Regexp(regex='^[a-zA-Z ]+$', message='El nombre solo puede contener letras')
instructor_validator = validators.Regexp(regex='^[a-zA-Z0-9, ]+$', message='El nombre de un instructor solo puede contener letras y numeros, por favor separe los nombres de varios instructores con una coma')

class DisciplineForm(FlaskForm):    
    name = StringField('Nombre', validators=[alphabetic_validator,Length(max=255),InputRequired()])
    category = StringField('Categoría',validators=[Length(max=255),InputRequired()])
    instructors= StringField('Instructores',validators=[Length(max=255),InputRequired(),instructor_validator],description="Separe los nombres de los instructores con una coma")
    dates = StringField('Días y horarios',validators=[Length(max=255),InputRequired()])
    monthly_cost = DecimalField('Costo mensual',validators=[InputRequired()])
    available = SelectField('Disponible',choices=[(True,'Disponible'),('False','No disponible')],validators=[InputRequired()])
