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

# Get some objects
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


@app.route("/")
def index():
	if len(infoVuelo) and len(infoPasajeros):
		db.createDB()
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
		
		items = []
		for row in query:
			items.append(Item('Numero de vuelo', row[0]))
			items.append(Item('Ciudad de salida', row[1]))
			items.append(Item('Ciudad de llegada', row[2]))
			items.append(Item('Numero de puestos', row[3]))
			items.append(Item('ID piloto', row[4]))
			items.append(Item('ID pasajero', row[5]))	

		# Populate the table
		table = ItemTable(items)

		# Print the html
		render_template(table.__html__())

	return render_template("consultarPorNumero.html",form = form)








def main():
	app.run(debug = True, port = 8000)

main()