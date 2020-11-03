class Persona(object):
	"""
	Clase que representa a una persona
	"""

	def __init__(self, nombre):
		self.nombre = nombre

	def getNombre(self):
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

	def getHorasVuelo(self):
		return self.horasVuelo

	def getId(self):
		return self.id

	def verPiloto(self):
		return [self.getId(),self.getNombre(),self.getHorasVuelo()]

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

	def getEdad(self):
		return self.edad

	def getGenero(self):
		return self.genero

	def setEdad(self,e):
		self.edad = e
	
	def setGenero(self,g):
		self.genero = g

	def getId(self):
		return self.id
	def getNroVuelo(self):
		return self.nroVuelo

	def verPasajero(self):
		return [self.getId(),self.getNombre(),self.getEdad(),self.getGenero(),self.getNroVuelo()]