def copia(fichero):
	""" 
	Se pasa por parámetro el nombre del fichero.
	Crea dos ficheros, uno con nombre del fichero y otro con extensión bak.
	Copia del archivo creado el contenido al archivo bak.
	"""
	fichero1 = open(str(fichero), "w+")
	fichero2 = open(str(fichero) + "bak.txt", "w+")

	respuesta = ""
	while(respuesta != "n"):
		respuesta = input("Introduce texto para fichero: ")
		fichero1.write(respuesta + "\n")
		respuesta = input("¿Otra línea s/n?: ")
	print("El fichero y su copia se ha creado.")	
	fichero1.close()
	fichero1 = open(fichero, "r")

	for linea in fichero1:
		fichero2.write(linea)
	fichero1.close()
	fichero2.close()

fichero = input("Introduce nombre del fichero: ")
copia(fichero)		