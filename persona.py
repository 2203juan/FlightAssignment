class Persona(object):
	"""
	Clase que representa a una persona
	"""

	def __init__(self, nombre):
		self.nombre = nombre

	def get_Nombre(self):
		return self.nombre

class Piloto(Persona):
	"""
	Clase que representa a un piloto de la compañia
	"""
	def __init__(self, id, nombre, horasVuelo):

		# Se invoca al constructor de la clase persona

		Persona.__init__(self, nombre)
		self.horasVuelo = horasVuelo
		self.id = id

	def setHorasVuelo(self, h):
		self.horasVuelo = h

	def get_HorasVuelo(self):
		return self.horasVuelo

	def get_Id(self):
		return self.id

	def verPiloto(self):
		return [self.get_Id(),self.get_Nombre(),self.get_HorasVuelo()]

class Pasajero(Persona):
	"""
	Clase que representa a un pasajero 
	"""

	def __init__(self, cedula, nombre, edad, genero, nroVuelo):

		# Se invoca al constructor de la clase persona
		Persona.__init__(self,nombre)
		self.edad = edad
		self.genero = genero # 0 para hombre 1 para mujer
		self.id = cedula
		self.nroVuelo = nroVuelo

	def get_Edad(self):
		return self.edad

	def get_Genero(self):
		return self.genero

	def setEdad(self,e):
		self.edad = e
	
	def setGenero(self,g):
		self.genero = g

	def get_Id(self):
		return self.id
	def get_NroVuelo(self):
		return self.nroVuelo

	def verPasajero(self):
		return [self.get_Id(),self.get_Nombre(),self.get_Edad(),self.get_Genero(),self.get_NroVuelo()]