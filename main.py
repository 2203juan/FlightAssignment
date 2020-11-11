from flask import Flask
from flask import render_template
from flask import request
from flask import  url_for
from flask import redirect
import forms
import vuelo as v
import persona as p
import DB as db
import login as lg
from flask_wtf.csrf import CSRFProtect


infoVuelo = list()
infoPasajeros = list()

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
csrf = CSRFProtect()
csrf.init_app(app) # Compliant



@app.route("/index")
def index():
	if len(infoVuelo) and len(infoPasajeros):
		ciudad_a =  infoVuelo[0]
		ciudad_b = infoVuelo[1]
		numero_puestos = infoVuelo[2]
		numero_vuelo = infoVuelo[3] 
		nombre_piloto = infoVuelo[4] 
		horas_vuelo_piloto = infoVuelo[5]
		id_piloto = infoVuelo[6]

		piloto = p.Piloto(id_piloto,nombre_piloto, horas_vuelo_piloto)
		vuelo = v.Vuelo(numero_vuelo,ciudad_a,ciudad_b,piloto,numero_puestos)

		for pasajero in infoPasajeros:
			cedula = pasajero[0]
			nombrePasajero = pasajero[1]
			edad = pasajero[2]
			sexo = int(pasajero[3])

			pasajero = p.Pasajero(cedula,nombrePasajero,edad,sexo,numero_vuelo)
			vuelo.agregar_pasajero(pasajero)
			piloto = vuelo.get_piloto()

		pasajeros = vuelo.get_pasajeros()

		for pasajero in pasajeros:
			db.crearPasajero(pasajero.verPasajero())

			numeroVuelo = vuelo.get_numero_vuelo()
			ciudad_a = vuelo.get_ciudad_salida()
			ciudad_b = vuelo.get_ciudad_llegada()
			numero_puestos = vuelo.get_numero_puestos()
			id_piloto = piloto[0]
			idPasajero = pasajero.get_id()
			vuelotmp = (numeroVuelo,ciudad_a,ciudad_b,numero_puestos,id_piloto,idPasajero)

			db.insertarVuelo(vuelotmp)

		db.crearPiloto(piloto)

		infoVuelo.clear()
		infoPasajeros.clear()
	return render_template("index.html")

@app.route("/registrarVuelo", methods=["GET", "POST"])
def vuelo():
	form = forms.FlyForm()
	if form.validate_on_submit():
		ciudad_a = form.ciudad_a.data
		ciudad_b = form.ciudad_b.data
		numero_puestos = form.numero_puestos.data
		numero_vuelo = form.numero_vuelo.data
		nombre_piloto = form.nombre_piloto.data
		horas_vuelo_piloto = form.horas_vuelo_piloto.data
		id_piloto = form.id_piloto.data

		infoVuelo.append(ciudad_a)
		infoVuelo.append(ciudad_b)
		infoVuelo.append(numero_puestos)
		infoVuelo.append(numero_vuelo)
		infoVuelo.append(nombre_piloto)
		infoVuelo.append(horas_vuelo_piloto)
		infoVuelo.append(id_piloto)

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
		nombre_pasajero = form.nombre_pasajero.data
		edad = form.edad.data
		sexo = form.sexo.data

		tmp = list()
		tmp.append(cedula)
		tmp.append(nombre_pasajero)
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
		numero_vuelo = form.numero_vuelo.data
		query = db.query("SELECT * FROM VUELO WHERE numeroVuelo = {}".format(numero_vuelo))
		
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
	form = forms.PilotoForm()
	if form.validate_on_submit():
		id_piloto = form.id_piloto.data
		query = db.query("SELECT numeroVuelo,ciudadSalida,ciudadLlegada FROM VUELO WHERE idPiloto = {}".format(id_piloto))
		
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

@app.route('/', methods=['GET', 'POST'])
def login():
	form = lg.LoginForm()

	if form.validate_on_submit():
		db.insertarAdmin(('juanhu2203@gmail.com','Pruebas2020'))
		real = db.query("SELECT * FROM ADMIN")
		user = form.email.data
		password = form.password.data
		if user == real[0][0] and password == real[0][1]:
			return redirect(url_for('index'))
			
	return render_template('login.html', form = form)
@app.route('/about')
def about():
	return render_template('sobre_nosotros.html')

@app.route('/reserva',methods = ['GET', 'POST'])
def reserva():
	form = forms.buyForm()
	if form.validate_on_submit():

		ciudades = {"1":'Medellin', "2":'Bogota',"3":'Cali',"4":'San Andrés',"5":'Cartagena'}
		nombre = form.nombre.data
		cedula = form.cedula.data
		edad = form.edad.data
		ciudad_a = form.ciudad_a.data
		ciudad_b = form.ciudad_b.data
		cantidadPersonas = form.cantidadPersonas.data

		monto_base = 300000
		descuento = 0 


		if ciudad_a == "1" or ciudad_a == "2" or ciudad_a == "3":
			descuento += 0.2# si la ciudad de salida es Medellin,Bogota o Cali se descuenta un 20%

		if  1<= edad <= 5:
			descuento += 0.6

		if 5 < edad <= 10:
			descuento += 0.3
		
		if  10 < edad	<= 18:
			descuento += 0.2


		monto_por_persona = monto_base*(1-descuento)

		if cantidadPersonas > 3:
			monto_por_persona = monto_por_persona*(1-0.1)

		montoTotal = cantidadPersonas*monto_por_persona

		montoTotal  = "${:,.2f}".format(montoTotal)



		items = {"Nombre": nombre,"Cedula": cedula, "Edad": edad,"Ciudad de Salida":ciudades[ciudad_a],"Ciudad de Llegada":ciudades[ciudad_b],"Nro Personas": cantidadPersonas,"Monto Reserva": montoTotal}

		print(items)
		return render_template("confirmacion.html", result = items)

	return render_template("reserva.html", form = form)

@app.route('/reserva_equipaje',methods = ['GET', 'POST'])
def reserva_equipaje():
	form = forms.luggageForm()
	if form.validate_on_submit():

		cedula = form.cedula.data
		peso = form.peso.data

		monto_base = 60000
		excedente = 0

		# entre 1 y 23 kg vale 60.000

		# por cada kg adicional se cobran 3000 pesos
		if 23 < peso <= 50:
			excedente = (peso - 23)*3000

		# por cada kg adicional se cobran 5000 pesos
		elif 50< peso <=70:
			excedente = (peso-20)*5000

		# por cada kg adicional se cobran 5000 pesos
		else:
			excedente = (peso -70)*7000




		montoTotal = monto_base + excedente

		montoTotal  = "${:,.2f}".format(montoTotal)



		items = {"Cedula": cedula, "Monto Reserva Equipaje": montoTotal}

		print(items)
		return render_template("confirmacion_equipaje.html", result = items)

	return render_template("reserva_equipaje.html", form = form)

def main():
	app.run(debug = True, port = 8080)

main()