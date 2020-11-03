from flask import Flask
from flask import render_template
from flask import request
from flask import  url_for
from flask import redirect
import forms


app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'


@app.route("/")
def index():
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

		print(ciudadA)
		print(ciudadB)
		print(nroPuestos)
		print(nroVuelo)
		print(nombrePiloto)
		print(horasVueloPiloto)
		print(idPiloto)

		return redirect(url_for('pasajeros'))

	return render_template("registrarVuelo.html",form = form)
@app.route("/pasajeros")
def pasajeros():
	return render_template("index.html")


	

def main():
	app.run(debug = True, port = 8000)

main()