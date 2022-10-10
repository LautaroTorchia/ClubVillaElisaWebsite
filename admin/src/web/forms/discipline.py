from wtforms import StringField, DecimalField, SelectField, Label
from wtforms.validators import Length, InputRequired, NumberRange, Regexp
from src.web.forms.base_form import BaseForm

instructor_validator = Regexp(regex='^(?:[^\W\d_]|[ ,])+$', message='El nombre de un instructor solo puede contener letras y numeros, por favor separe los nombres de varios instructores con una coma')

class DisciplineForm(BaseForm):

    name = StringField('Nombre', validators=[BaseForm.alphabetic_validator,Length(max=255),InputRequired()])
    category = StringField('Categoría',validators=[Length(max=255),InputRequired()])
    instructors= StringField('Instructores',validators=[Length(max=255),InputRequired(),instructor_validator],description="Separe los nombres de los instructores con una coma")
    dates = StringField('Días y horarios',validators=[Length(max=255),InputRequired()])
    monthly_cost = DecimalField("Costo mensual",validators=[InputRequired(),NumberRange(0,message="El costo mensual debe ser mayor a 0")])
    available = SelectField('Disponible',choices=[(True,'Disponible'),('False','No disponible')],validators=[InputRequired()])

    def __init__(self, formdata=..., **kwargs):
        super().__init__( **kwargs)
        try:
            self['monthly_cost'].label = Label(self['monthly_cost'].id, f"Costo mensual ({kwargs['currency']})")
        except:
            pass
        