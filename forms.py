from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField
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

def cedulaCheck(form,field):
	try:
		number = field.data

		if number < 1000000000 or number > 9999999999:
			raise ValidationError('It should be a number between 10000 and 99999!!')
	except Exception as e:
		raise ValidationError('It should be a number between 1000000000 and 9999999999!!')

def edadCheck(form,field):
	try:
		number = field.data

		if number < 0 or number > 150:
			raise ValidationError('It should be a number between 10000 and 99999!!')
	except Exception as e:
		raise ValidationError('It should be a number between 0 and 150!!')

class FlyForm(FlaskForm):
    ciudadA = StringField('Ciudad de Salida:', validators = [DataRequired(), Length(max=64)])
    ciudadB = StringField('Ciudad de Llegada:', validators = [DataRequired(), Length(max=64)])
    nroPuestos = IntegerField('Numero de puestos:', validators = [nroPuestoscheck] )
    nroVuelo = IntegerField('Numero de vuelo:', validators = [nroVueloCheck] )
    nombrePiloto = StringField('Nombre del piloto:', validators = [DataRequired(), Length(max=64)])
    horasVueloPiloto = IntegerField('Horas de vuelo del piloto:', validators = [nroVueloCheck] )
    idPiloto = IntegerField('ID del piloto:', validators = [nroVueloCheck] )
    submit = SubmitField('Continuar')

class PasForm(FlaskForm):
	cedula = IntegerField('Cedula:', validators = [cedulaCheck] )
	nombrePasajero = StringField('Nombre del pasajero:', validators = [DataRequired(), Length(max=64)])
	edad = IntegerField('Edad:', validators = [edadCheck] )
	sexo = RadioField('Sexo:', choices = [(0,'hombre'),(1,'mujer')],validators = [DataRequired()])
	submit = SubmitField('Continuar')

class numeroVueloForm(FlaskForm):
	nroVuelo = IntegerField('Numero de vuelo:', validators = [nroVueloCheck] )
	submit = SubmitField('Consultar')
