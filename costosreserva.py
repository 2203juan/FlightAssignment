def calcular_valor_reserva(ciudad_a, edad, cantidad_personas):
	monto_base = 300000 # monto base para cualquier vuelo nacional
	descuento = 0 

	# primer descuento posible
	if ciudad_a == "MEDELLIN" or ciudad_a == "CALI" or ciudad_a == "BOGOTA":
		descuento += 0.2# si la ciudad de salida es Medellin,Bogota o Cali se descuenta un 20%

	# segundo descuento posible
	if  1 <= edad <= 5:
		descuento += 0.6

	if 5 < edad <= 10:
		descuento += 0.3
	
	if  10 < edad	<= 18:
		descuento += 0.2

	# tercer descuento posible
	if cantidad_personas > 3:
		descuento += 0.1

	# se calcula el monto por persona haciendo el respectivo descuento
	monto_por_persona = monto_base * (1-descuento)

	# se calcula el monto total
	monto_total = cantidad_personas * monto_por_persona

	monto_total  = "${:,.2f}".format(monto_total)

	descuento = str(int(descuento*100)) + "%"

	return monto_total, descuento

def calcular_valor_reserva_equipaje(peso):
	monto_base = 60000 # entre 1 y 23 kg vale 60.000
	excedente = 0 # se guarda el pago adicional si se pasa de 23kg

	# si el peso del equipaje no supera los 50kg se cobra 20% de excedente
	if 23 <= peso <= 50:
		excedente = 0.2

	# si el peso del equipaje no supera los 70kg se cobra 40% de excedente
	elif 50 < peso <= 70:
		excedente = 0.4

	# si el peso del equipaje no supera los 50kg se cobra 20% de excedente
	elif 70 < peso <= 100:
		excedente = 0.6
	else:

		excedente = 1.5


	# se calcula el monto total
	monto_total = monto_base * (1 + excedente)
	
	monto_total  = "${:,.2f}".format(monto_total)

	excedente = str(int(excedente*100)) + "%"

	return monto_total, excedente
