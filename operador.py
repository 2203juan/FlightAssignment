import vuelo as v
import persona as p
import DB as db

def main():
	db.createDB()
	print("Bienvenido al sistema de vuelos")
	op = int(input("1) Crear Vuelo\n2)Salir\n\n"))

	while op!=2:
		
		ciudadSalida = input("Ingrese la ciudad de Salida:\n")
		ciudadLlegada = input("Ingrese la ciudad de Llegada\n")
		numeroPuestos = int(input("Ingrese el numero de puestos que tiene el avion\n"))
		numeroVuelo = int(input("Ingrese el numero del vuelo\n"))

		while numeroVuelo < 0:
			print("Numero invalido!!")
			numeroVuelo = int(input("Ingrese el numero del vuelo\n"))


		while numeroPuestos < 200:
			print("El minimo numero de puestos permitidos es 200")
			numeroPuestos = int(input("Ingrese el numero de puestos que tiene el avion\n"))

		nombrePiloto = input("Ingrese el nombre del Piloto\n")
		horasVuelo = int(input("Ingrese la cantidad de horas de vuelo que tiene el piloto\n"))

		while horasVuelo <=0:
			print("El minimo de horas de vuelo permitido es 1")
			horasVuelo = int(input("Ingrese la cantidad de horas de vuelo que tiene el piloto\n"))

		print("Ingrese el id del piloto")
		idPiloto = int(input())

		while idPiloto < 0:
			print("id Invalido!!")
			print("Ingrese el id del piloto")
			idPiloto = int(input())

		piloto = p.Piloto(idPiloto,nombrePiloto, horasVuelo)


		vuelo = v.Vuelo(numeroVuelo,ciudadSalida,ciudadLlegada,piloto,numeroPuestos)


		cantidadPasajeros = int(input("Ingrese la cantidad de pasajeros\n"))
		while cantidadPasajeros < 0:
			print("La cantidad de pasajeros no puede ser negativa")
			cantidadPasajeros = int(input("Ingrese la cantidad de pasajeros"))

		while cantidadPasajeros > numeroPuestos:
			print("El numero de puestos disponibles es: ",numeroPuestos)
			cantidadPasajeros = int(input("Ingrese la cantidad de pasajeros"))

		for i in range(cantidadPasajeros):
			print("Ingrese el nombre del pasajero",i+1)
			nombre = input()

			print("Ingrese la edad del pasajero",i+1)
			edad = int(input())

			while edad < 0:
				print("La edad no puede ser negativa")
				print("Ingrese la edad del pasajero",i+1)
				edad = int(input())

			print("Ingrese el sexo del pasajero 0-hombre 1-mujer")
			sexo = int(input())

			while sexo < 0 and sexo > 1:
				print("Invalido!!")
				print("Ingrese el sexo del pasajero 0-hombre 1-mujer")
				sexo = int(input())

			print("Ingrese la cedula del pasajero")
			cedula = int(input())

			while cedula < 0:
				print("Cedula invalida!!")
				print("Ingrese la cedula del pasajero")
				cedula = int(input())

			pasajero = p.Pasajero(cedula,nombre,edad,sexo,numeroVuelo)

			vuelo.agregarPasajero(pasajero)
			# una vez cargada toda la info la almacenamos en la base de datos
		piloto = vuelo.getPiloto()

		pasajeros = vuelo.getPasajeros()

		for pasajero in pasajeros:
			db.crearPasajero(pasajero.verPasajero())

			numeroVuelo = vuelo.getNroVuelo()
			ciudadA = vuelo.getCiudadSalida()
			ciudadB = vuelo.getCiudadLlegada()
			nroPuestos = vuelo.getNumeroPuestos()
			idPiloto = piloto[0]
			idPasajero = pasajero.getId()
			vuelotmp = (numeroVuelo,ciudadA,ciudadB,nroPuestos,idPiloto,idPasajero)

			db.insertarVuelo(vuelotmp)

		db.crearPiloto(piloto)


		op = int(input("1) Crear Vuelo\n2)Salir\n\n"))




main()
db.query("SELECT * FROM VUELO")
print()
db.query("SELECT * FROM VUELO WHERE VUELO.numeroVuelo = 4444444444")