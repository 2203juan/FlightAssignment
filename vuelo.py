import persona as p

class Vuelo(object):

	def __init__(self, nroVuelo, ciudadSalida, ciudadLlegada, piloto, numeroPuestos):
		self.ciudadSalida = ciudadSalida
		self.ciudadLlegada = ciudadLlegada
		self.piloto = piloto
		self.numeroPuestos = numeroPuestos
		self.pasajeros = list()
		self.nroVuelo = nroVuelo

	def get_ciudadSalida(self):
		return self.ciudadSalida

	def get_ciudadLlegada(self):
		return self.ciudadLlegada

	def get_numeroPuestos(self):
		return self.numeroPuestos

	def get_piloto(self):
		return self.piloto.verPiloto()

	def agregarPasajero(self, p):
		self.pasajeros.append(p)

	def get_pasajeros(self):
		return self.pasajeros

	def get_nroVuelo(self):
		return self.nroVuelo

	def verVuelo(self):
		return [self.get_nroVuelo(),self.get_ciudadSalida(), self.get_ciudadLlegada(), self.get_numeroPuestos(), self.get_piloto(), self.get_pasajeros()]

"""
def main():
	pil1 = p.Piloto("Juan Hoyos",472)
	v1 = Vuelo("Cali","Medellin",pil1,350)

	pa1 = p.Pasajero("Jeison",22,0)
	pa2 = p.Pasajero("Julian",27,0)

	v1.agregarPasajero(pa1)
	v1.agregarPasajero(pa2)
	print(v1.verVuelo())
main()
"""