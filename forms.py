from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length,NumberRange,ValidationError



def nroPuestoscheck(form,field):
	try:
		number = field.data

		if number < 200 or number > 480:
			raise ValidationError('It should be a number between 200 and 480!!')
	except Exception as e:
		raise ValidationError('It should be a number between 200 and 480!!')

def nroVueloCheck(form,field):
	try:
		number = field.data

		if number < 10000 or number > 99999:
			raise ValidationError('It should be a number between 10000 and 99999!!')
	except Exception as e:
		raise ValidationError('It should be a number between 10000 and 99999!!')



class FlyForm(FlaskForm):
    ciudadA = StringField('Ciudad de Salida:', validators = [DataRequired(), Length(max=64)])
    ciudadB = StringField('Ciudad de Llegada:', validators = [DataRequired(), Length(max=64)])
    nroPuestos = IntegerField('Numero de puestos:', validators = [nroPuestoscheck] )
    nroVuelo = IntegerField('Numero de vuelo:', validators = [nroVueloCheck] )
    nombrePiloto = StringField('Nombre del piloto:', validators = [DataRequired(), Length(max=64)])
    horasVueloPiloto = IntegerField('Horas de vuelo del piloto:', validators = [nroVueloCheck] )
    idPiloto = IntegerField('ID del piloto:', validators = [nroVueloCheck] )
    submit = SubmitField('Continuar')