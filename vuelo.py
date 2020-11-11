import persona as p

class Vuelo(object):

	def __init__(self, numero_vuelo, ciudad_salida, ciudad_llegada, piloto, numero_puestos):
		self.ciudad_salida = ciudad_salida
		self.ciudad_llegada = ciudad_llegada
		self.piloto = piloto
		self.numero_puestos = numero_puestos
		self.pasajeros = list()
		self.numero_vuelo = numero_vuelo

	def get_ciudad_salida(self):
		return self.ciudad_salida

	def get_ciudad_llegada(self):
		return self.ciudad_llegada

	def get_numero_puestos(self):
		return self.numero_puestos

	def get_piloto(self):
		return self.piloto.verPiloto()

	def agregar_pasajero(self, p):
		self.pasajeros.append(p)

	def get_pasajeros(self):
		return self.pasajeros

	def get_numero_vuelo(self):
		return self.numero_vuelo

	def ver_vuelo(self):
		return [self.get_numero_vuelo(),self.get_ciudad_salida(), self.get_ciudad_llegada(), self.get_numero_puestos(), self.get_piloto(), self.get_pasajeros()]
