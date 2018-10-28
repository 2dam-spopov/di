def area_triangulo(a,b):
	"""Calcula área de un triángulo"""
	area=(a*b)/2
	return area

while True:
	try:
		a = float(input("Introduce altura del triángulo: "))
		b = float(input("Introduce base del triángulo: "))
		break
	except ValueError:
		print("Debes introducir un número!")

triangulo_area=area_triangulo(a,b)

print("El área del triángulo es:", triangulo_area)	