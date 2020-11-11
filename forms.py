from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Length,NumberRange,ValidationError



def numero_puestos_check(form,field):
	try:
		number = field.data

		if number < 200 or number > 480:
			raise ValidationError('It should be a number between 200 and 480!!')
	except Exception:
		raise ValidationError('It should be a number between 200 and 480!!')

def numero_vuelo_check(form,field):
	try:
		number = field.data

		if number < 10000 or number > 99999:
			raise ValidationError('It should be a number between 10000 and 99999!!')
	except Exception:
		raise ValidationError('It should be a number between 10000 and 99999!!')

def cedula_check(form,field):
	try:
		number = field.data

		if number < 1000000000 or number > 9999999999:
			raise ValidationError('It should be a number between 10000 and 99999!!')
	except Exception:
		raise ValidationError('It should be a number between 1000000000 and 9999999999!!')

def edad_check(form,field):
	try:
		number = field.data

		if number < 0 or number > 150:
			raise ValidationError('It should be a number between 10000 and 99999!!')
	except Exception:
		raise ValidationError('It should be a number between 0 and 150!!')

class FlyForm(FlaskForm):
    ciudad_a = StringField('Ciudad de Salida:', validators = [DataRequired(), Length(max=64)])
    ciudad_b = StringField('Ciudad de Llegada:', validators = [DataRequired(), Length(max=64)])
    numero_puestos = IntegerField('Numero de puestos:', validators = [numero_puestos_check] )
    numero_vuelo = IntegerField('Numero de vuelo:', validators = [numero_vuelo_check] )
    nombre_piloto = StringField('Nombre del piloto:', validators = [DataRequired(), Length(max=64)])
    horas_vuelo_piloto = IntegerField('Horas de vuelo del piloto:', validators = [numero_vuelo_check] )
    id_piloto = IntegerField('ID del piloto:', validators = [numero_vuelo_check] )
    submit = SubmitField('Continuar')

class PasForm(FlaskForm):
	cedula = IntegerField('Cedula:', validators = [cedula_check] )
	nombre_pasajero = StringField('Nombre del pasajero:', validators = [DataRequired(), Length(max=64)])
	edad = IntegerField('Edad:', validators = [edad_check] )
	sexo = RadioField('Sexo:', choices = [(0,'hombre'),(1,'mujer')],validators = [DataRequired()])
	submit = SubmitField('Continuar')

class numeroVueloForm(FlaskForm):
	numero_vuelo = IntegerField('Numero de vuelo:', validators = [numero_vuelo_check] )
	submit = SubmitField('Consultar')

class PilotoForm(FlaskForm):
	id_piloto = IntegerField('Id piloto:', validators = [numero_vuelo_check] )
	submit = SubmitField('Consultar')

class buyForm(FlaskForm):
	nombre = StringField('Nombre :', validators = [DataRequired(), Length(max=64)])
	cedula = IntegerField('Cedula:', validators = [cedula_check] )
	edad = IntegerField('Edad:', validators = [edad_check] )
	ciudad_a = SelectField(u'Ciudad de Salida', choices=[(1, 'Medellin'), (2, 'Bogota'), (3, 'Cali'), (4, 'San Andrés'), (5, 'Cartagena')])
	ciudad_b = SelectField(u'Ciudad de Llegada', choices=[(1, 'Medellin'), (2, 'Bogota'), (3, 'Cali'), (4, 'San Andrés'), (5, 'Cartagena')])
	cantidad_personas = IntegerField('Cantidad de personas:', validators = [edad_check] )
	submit = SubmitField('Reservar')

class luggageForm(FlaskForm):
	cedula = IntegerField('Cedula:', validators = [cedula_check] )
	peso = IntegerField('Peso (Kg) del equipaje:', validators = [edad_check] )
	submit = SubmitField('Reservar')