print("Asinaturas 2019")
print("Informatica - Software - Usabilidad")
opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()
if asignatura in ("informatica", "software", "usabilidad"):
	print("Asignatura elegida " + asignatura)
else:
	print("No disponible")
