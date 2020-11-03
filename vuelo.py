import persona as p

class Vuelo(object):

	def __init__(self, nroVuelo, ciudadSalida, ciudadLlegada, piloto, numeroPuestos):
		self.ciudadSalida = ciudadSalida
		self.ciudadLlegada = ciudadLlegada
		self.piloto = piloto
		self.numeroPuestos = numeroPuestos
		self.pasajeros = list()
		self.nroVuelo = nroVuelo

	def getCiudadSalida(self):
		return self.ciudadSalida

	def getCiudadLlegada(self):
		return self.ciudadLlegada

	def getNumeroPuestos(self):
		return self.numeroPuestos

	def getPiloto(self):
		return self.piloto.verPiloto()

	def agregarPasajero(self, p):
		self.pasajeros.append(p)

	def getPasajeros(self):
		return self.pasajeros

	def getNroVuelo(self):
		return self.nroVuelo

	def verVuelo(self):
		return [self.getNroVuelo(),self.getCiudadSalida(), self.getCiudadLlegada(), self.getNumeroPuestos(), self.getPiloto(), self.getPasajeros()]

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