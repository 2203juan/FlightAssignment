from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Length,NumberRange,ValidationError

#constantes
error_no_vacio = "Este campo es obligatorio"
cedula = 'Cedula:'

def numero_puestos_check(form,field):
	error_numero_puestos = 'El numero de puestos debe estar entre 200 y 480!!'
	try:
		number = field.data

		if number < 200 or number > 480:
			raise ValidationError(error_numero_puestos)
	except Exception:
		raise ValidationError(error_numero_puestos)

def numero_vuelo_check(form,field):
	error_numero_vuelo = 'El numero de vuelo debe ser un numero positivo!!'
	try:
		number = field.data

		if number <= 0:
			raise ValidationError(error_numero_vuelo)
	except Exception:
		raise ValidationError(error_numero_vuelo)

def cedula_check(form,field):
	error_cedula = "El numero de cedula debe ser un numero positivo!!"
	try:
		number = field.data

		if number <= 0:
			raise ValidationError(error_cedula)
	except Exception:
		raise ValidationError(error_cedula)

def edad_check(form,field):
	error_edad = "La edad debe ser un numero entero entre 0 y 150!!"
	try:
		number = field.data

		if number < 0 or number > 150:
			raise ValidationError(error_edad)
	except Exception:
		raise ValidationError(error_edad)

def horas_vuelo_check(form,field):
	error_horas_vuelo = "El minimo de horas requerido es 200!!"
	try:
		number = field.data

		if number < 200:
			raise ValidationError(error_horas_vuelo)
	except Exception:
		raise ValidationError(error_horas_vuelo)

def id_piloto_check(form,field):
	error_id_piloto = "El id del piloto debe ser un numero positivo!!"
	try:
		number = field.data

		if number <= 0:
			raise ValidationError(error_id_piloto)
	except Exception:
		raise ValidationError(error_id_piloto)

def cantidad_personas_check(form,field):
	error_cantidad_personas = 'El numero de personas debe ser un numero positivo!!'
	try:
		number = field.data

		if number <=0 :
			raise ValidationError(error_cantidad_personas)
	except Exception:
		raise ValidationError(error_cantidad_personas)

def peso_check(form,field):
	error_peso = 'El peso debe der un numero entero positivo!!'
	try:
		number = field.data

		if number <= 0:
			raise ValidationError(error_peso)
	except Exception:
		raise ValidationError(error_peso)

class FlyForm(FlaskForm):
    ciudad_a = StringField('Ciudad de Salida:', validators = [DataRequired(message = error_no_vacio), Length(max=64)])
    ciudad_b = StringField('Ciudad de Llegada:', validators = [DataRequired(message = error_no_vacio), Length(max=64)])
    numero_puestos = IntegerField('Numero de puestos:', validators = [numero_puestos_check] )
    numero_vuelo = IntegerField('Numero de vuelo:', validators = [numero_vuelo_check] )
    nombre_piloto = StringField('Nombre del piloto:', validators = [DataRequired(message = error_no_vacio), Length(max=64)])
    horas_vuelo_piloto = IntegerField('Horas de vuelo del piloto:', validators = [horas_vuelo_check] )
    id_piloto = IntegerField('ID del piloto:', validators = [id_piloto_check] )
    submit = SubmitField('Continuar')

class PasForm(FlaskForm):
	cedula = IntegerField(cedula, validators = [cedula_check] )
	nombre_pasajero = StringField('Nombre del pasajero:', validators = [DataRequired(message = error_no_vacio), Length(max=64)])
	edad = IntegerField('Edad:', validators = [edad_check] )
	sexo = RadioField('Sexo:', choices = [(0,'hombre'),(1,'mujer')],validators = [DataRequired(message = error_no_vacio)])
	submit = SubmitField('Continuar')

class NumeroVueloForm(FlaskForm):
	numero_vuelo = IntegerField('Numero de vuelo:', validators = [numero_vuelo_check] )
	submit = SubmitField('Consultar')

class PilotoForm(FlaskForm):
	id_piloto = IntegerField('Id piloto:', validators = [id_piloto_check])
	submit = SubmitField('Consultar')

class BuyForm(FlaskForm):
	nombre = StringField('Nombre :', validators = [DataRequired(message = error_no_vacio), Length(max=64)])
	cedula = IntegerField(cedula, validators = [cedula_check] )
	edad = IntegerField('Edad:', validators = [edad_check] )
	ciudad_a = SelectField(u'Ciudad de Salida', choices=[(1, 'Medellin'), (2, 'Bogota'), (3, 'Cali'), (4, 'San Andrés'), (5, 'Cartagena')])
	ciudad_b = SelectField(u'Ciudad de Llegada', choices=[(1, 'Medellin'), (2, 'Bogota'), (3, 'Cali'), (4, 'San Andrés'), (5, 'Cartagena')])
	cantidad_personas = IntegerField('Cantidad de personas:', validators = [cantidad_personas_check] )
	submit = SubmitField('Reservar')

class LuggageForm(FlaskForm):
	cedula = IntegerField(cedula, validators = [cedula_check] )
	peso = IntegerField('Peso (Kg) del equipaje:', validators = [peso_check] )
	submit = SubmitField('Reservar')