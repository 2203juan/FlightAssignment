def calcular_valor_reserva(ciudad_a, edad, cantidad_personas):
	monto_base = 300000 # monto base para cualquier vuelo nacional
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

	if cantidad_personas > 3:
		monto_por_persona = monto_por_persona*(1-0.1)

	monto_total = cantidad_personas*monto_por_persona

	monto_total  = "${:,.2f}".format(monto_total)

	return monto_total

def calcular_valor_reserva_equipaje(peso):
	monto_base = 60000 # entre 1 y 23 kg vale 60.000
	excedente = 0 # se guarda el pago adicional si se pasa de 23kg

	# por cada kg adicional se cobran 3000 pesos
	if 23 <= peso <= 50:
		excedente = (peso - 23)*3000

	# por cada kg adicional se cobran 5000 pesos
	elif 50< peso <=70:
		excedente = (peso-20)*5000

	# por cada kg adicional se cobran 5000 pesos
	else:
		excedente = (peso -70)*7000



	monto_total = monto_base + excedente

	monto_total  = "${:,.2f}".format(monto_total)

	return monto_total