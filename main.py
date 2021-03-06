# se importan todos los modulos de flask
from flask import Flask
from flask import render_template
from flask import request
from flask import  url_for
from flask import redirect
from flask_wtf.csrf import CSRFProtect
# se importan los modulos desarrollados
import vuelo as v
import persona as p
import DB as db
import forms
import login as lg
import costosreserva as reserva


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
			nombre_pasajero = pasajero[1]
			edad = pasajero[2]
			sexo = int(pasajero[3])

			pasajero = p.Pasajero(cedula,nombre_pasajero,edad,sexo,numero_vuelo)
			vuelo.agregar_pasajero(pasajero)
			piloto = vuelo.get_piloto()

		pasajeros = vuelo.get_pasajeros()

		for pasajero in pasajeros:
			db.crear_pasajero(pasajero.verPasajero())

			numero_vuelo = vuelo.get_numero_vuelo()
			ciudad_a = vuelo.get_ciudad_salida()
			ciudad_b = vuelo.get_ciudad_llegada()
			numero_puestos = vuelo.get_numero_puestos()
			id_piloto = piloto[0]
			id_pasajero = pasajero.get_id()
			vuelotmp = (numero_vuelo,ciudad_a,ciudad_b,numero_puestos,id_piloto,id_pasajero)

			db.insertar_vuelo(vuelotmp)

		db.crear_piloto(piloto)

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
def registrar_pasajero():
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
def consultar_vuelo():
	return render_template("consultarVuelo.html")

@app.route("/consultarPorNumero", methods=["GET", "POST"])
def consultar_por_numero():
	form = forms.NumeroVueloForm()
	if form.validate_on_submit():
		numero_vuelo = form.numero_vuelo.data
		query = db.query("SELECT * FROM VUELO WHERE numeroVuelo = {}".format(numero_vuelo))
		key_numero_vuelo = 'Numero de vuelo'
		items = {
			key_numero_vuelo: list(),
			'Ciudad de salida': list(),
			'Ciudad de llegada': list(),
			'Numero de puestos': list(),
			'ID piloto': list(),
			'ID pasajero': list()

		}

		for row in query:
			if row[0] not in items[key_numero_vuelo]:
				items[key_numero_vuelo].append(row[0])
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
def consultar_por_piloto():
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

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = lg.LoginForm()

	if form.validate_on_submit():
		db.insertar_admin(('juanhu2203@gmail.com','Pruebas2020'))
		real = db.query("SELECT * FROM ADMIN")
		user = form.email.data
		password = form.password.data
		if user == real[0][0] and password == real[0][1]:
			return redirect(url_for('index'))
			
	return render_template('login.html', form = form)

@app.route('/cliente')
def cliente():
	return render_template('cliente.html')

@app.route('/')
def inicio():
	return render_template('menu.html')

@app.route('/about')
def about():
	return render_template('sobre_nosotros.html')

@app.route('/reserva',methods = ['GET', 'POST'])
def reserva_vuelo():
	form = forms.BuyForm()
	if form.validate_on_submit():

		
		nombre = form.nombre.data
		cedula = form.cedula.data
		edad = form.edad.data
		ciudad_a = form.ciudad_a.data.upper()
		ciudad_b = form.ciudad_b.data.upper()
		cantidad_personas = form.cantidad_personas.data

		monto_total, descuento = reserva.calcular_valor_reserva(ciudad_a, edad, cantidad_personas)

		items = {"Nombre": nombre,"Cedula": cedula, "Edad": edad,"Ciudad de Salida":ciudad_a,"Ciudad de Llegada":ciudad_b,"Nro Personas": cantidad_personas,"Monto Reserva": monto_total, "Descuento Aplicado": descuento}

		return render_template("confirmacion.html", result = items)

	return render_template("reserva.html", form = form)

@app.route('/reserva_equipaje',methods = ['GET', 'POST'])
def reserva_equipaje():
	form = forms.LuggageForm()
	if form.validate_on_submit():

		cedula = form.cedula.data
		peso = form.peso.data

		monto_total, excedente = reserva.calcular_valor_reserva_equipaje(peso)

		items = {"Cedula": cedula, "Monto Reserva Equipaje": monto_total, "Excedente Aplicado": excedente}

		return render_template("confirmacion_equipaje.html", result = items)

	return render_template("reserva_equipaje.html", form = form)

if __name__ == "__main__":
    app.run(debug = True)