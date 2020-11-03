from flask import Flask
from flask import render_template
from flask import request
from flask import  url_for
from flask import redirect
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/registrarVuelo", methods=["GET", "POST"])
def vuelo():
	if request.method == 'POST':
		ciudadA = request.form['ciudadA']
		ciudadB = request.form['ciudadB']
		nroPuestos = request.form["nroPuestos"]
		nroVuelo = request.form["nroVuelo"]
		nombrePiloto = request.form["nombrePiloto"]
		horasVueloPiloto = request.form["horasVueloPiloto"]
		idPiloto = request.form["idPiloto"]

		print(ciudadA)
		print(ciudadB)
		print(nroPuestos)
		print(nroVuelo)
		print(nombrePiloto)
		print(horasVueloPiloto)
		print(idPiloto)

		return redirect(url_for('pasajeros'))

	return render_template("registrarVuelo.html")
@app.route("/pasajeros")
def pasajeros():
	return render_template("index.html")


	

def main():
	app.run(debug = True, port = 8000)

main()