class Persona(object):
	"""
	Clase que representa a una persona
	"""

	def __init__(self, nombre):
		self.nombre = nombre

	def get_nombre(self):
		return self.nombre

class Piloto(Persona):
	"""
	Clase que representa a un piloto de la compañia
	"""
	def __init__(self, id, nombre, horas_vuelo):

		# Se invoca al constructor de la clase persona

		Persona.__init__(self, nombre)
		self.horas_vuelo = horas_vuelo
		self.id = id

	def setHo_vasVuelo(self, h):
		self.horas_vuelo = h

	def get_horas_vuelo(self):
		return self.horas_vuelo

	def get_id(self):
		return self.id

	def verPiloto(self):
		return [self.get_id(),self.get_nombre(),self.get_horas_vuelo()]

class Pasajero(Persona):
	"""
	Clase que representa a un pasajero 
	"""

	def __init__(self, cedula, nombre, edad, genero, numero_vuelo):

		# Se invoca al constructor de la clase persona
		Persona.__init__(self,nombre)
		self.edad = edad
		self.genero = genero # 0 para hombre 1 para mujer
		self.id = cedula
		self.numero_vuelo = numero_vuelo

	def get_edad(self):
		return self.edad

	def get_genero(self):
		return self.genero

	def setEdad(self,e):
		self.edad = e
	
	def setGenero(self,g):
		self.genero = g

	def get_id(self):
		return self.id
	def get_numero_vuelo(self):
		return self.numero_vuelo

	def verPasajero(self):
		return [self.get_id(),self.get_nombre(),self.get_edad(),self.get_genero(),self.get_numero_vuelo()]