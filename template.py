from flask import Flask
from flask import render_template
from flask import request
from flask import  url_for
from flask import redirect
import forms
import vuelo as v
import persona as p
import DB as db
from flask_table import Table, Col


infoVuelo = list()
infoPasajeros = list()
app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')


@app.route("/")
def index():
	if len(infoVuelo) and len(infoPasajeros):
		ciudadA =  infoVuelo[0]
		ciudadB = infoVuelo[1]
		nroPuestos = infoVuelo[2]
		nroVuelo = infoVuelo[3] 
		nombrePiloto = infoVuelo[4] 
		horasVueloPiloto = infoVuelo[5]
		idPiloto = infoVuelo[6]

		piloto = p.Piloto(idPiloto,nombrePiloto, horasVueloPiloto)
		vuelo = v.Vuelo(nroVuelo,ciudadA,ciudadB,piloto,nroPuestos)

		for pasajero in infoPasajeros:
			cedula = pasajero[0]
			nombrePasajero = pasajero[1]
			edad = pasajero[2]
			sexo = int(pasajero[3])

			pasajero = p.Pasajero(cedula,nombrePasajero,edad,sexo,nroVuelo)
			vuelo.agregarPasajero(pasajero)
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

		infoVuelo.clear()
		infoPasajeros.clear()
	return render_template("index.html")

@app.route("/registrarVuelo", methods=["GET", "POST"])
def vuelo():
	form = forms.FlyForm()
	if form.validate_on_submit():
		ciudadA = form.ciudadA.data
		ciudadB = form.ciudadB.data
		nroPuestos = form.nroPuestos.data
		nroVuelo = form.nroVuelo.data
		nombrePiloto = form.nombrePiloto.data
		horasVueloPiloto = form.horasVueloPiloto.data
		idPiloto = form.idPiloto.data

		infoVuelo.append(ciudadA)
		infoVuelo.append(ciudadB)
		infoVuelo.append(nroPuestos)
		infoVuelo.append(nroVuelo)
		infoVuelo.append(nombrePiloto)
		infoVuelo.append(horasVueloPiloto)
		infoVuelo.append(idPiloto)

		return redirect(url_for('pasajeros'))

	return render_template("registrarVuelo.html",form = form)
@app.route("/pasajeros")
def pasajeros():
	return render_template("pasajeros.html")

@app.route("/registrarPasajero",methods=["GET", "POST"])
def registrarPasajero():
	form = forms.PasForm()
	if form.validate_on_submit():
		cedula = form.cedula.data
		nombrePasajero = form.nombrePasajero.data
		edad = form.edad.data
		sexo = form.sexo.data

		tmp = list()
		tmp.append(cedula)
		tmp.append(nombrePasajero)
		tmp.append(edad)
		tmp.append(sexo)
		infoPasajeros.append(tmp)

		return redirect(url_for('pasajeros'))

	return render_template("registrarPasajero.html", form = form)



@app.route("/consultarVuelo")
def consultarVuelo():
	return render_template("consultarVuelo.html")

@app.route("/consultarPorNumero", methods=["GET", "POST"])
def consultarPorNumero():
	form = forms.numeroVueloForm()
	if form.validate_on_submit():
		nroVuelo = form.nroVuelo.data
		query = db.query("SELECT * FROM VUELO WHERE numeroVuelo = {}".format(nroVuelo))
		
		items = {
			'Numero de vuelo': list(),
			'Ciudad de salida': list(),
			'Ciudad de llegada': list(),
			'Numero de puestos': list(),
			'ID piloto': list(),
			'ID pasajero':list()

		}

		for row in query:
			if row[0] not in items['Numero de vuelo']:
				items['Numero de vuelo'].append(row[0])
				items['Ciudad de salida'].append(row[1])
				items['Ciudad de llegada'].append(row[2])
				items['Numero de puestos'].append(row[3])
				items['ID piloto'].append(row[4])

			items['ID pasajero'].append(row[5])	

		# Populate the table

		# Print the html

		return render_template("resultconsultarPorNumero.html", result = items)

	return render_template("consultarPorNumero.html",form = form)

@app.route("/consultarPorPiloto", methods=["GET", "POST"])
def consultarPorPiloto():
	form = forms.idPilotoForm()
	if form.validate_on_submit():
		idPiloto = form.idPiloto.data
		query = db.query("SELECT numeroVuelo,ciudadSalida,ciudadLlegada FROM VUELO WHERE idPiloto = {}".format(idPiloto))
		
		items = {}

		for row in query:
			print(row)
			if items.get(row[0])== None:
				items[row[0]] = (row[1],row[2])
		print(items)
		# Populate the table

		# Print the html

		return render_template("resultconsultarPorPiloto.html", result = items)
	

	return render_template("consultarPorPiloto.html",form = form)



def main():
	app.run(debug = True, port = 8000)

main()