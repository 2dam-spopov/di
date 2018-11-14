def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		#for subElemento in elemento:
		yield from elemento

ciudadesDevueltas=devuelveCiudades("Madrid","Barcelona","Valencia","Castellon")
print(next(ciudadesDevueltas))