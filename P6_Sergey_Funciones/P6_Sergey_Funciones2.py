#! /usr/bin/python3

def gcdIter(a,b):
	"""
	a: valor entero introducido por teclado.
	b: valor entero introducido por teclado.
	devuelve: el resultado de la oparción el MCD.
	"""
	while a>0:
		aux=a
		a=b%a;
		b=aux;
	return b	

while True:
	try:
		a = int(input("Introduzca a: "))
		b = int(input("Introduzca b: "))

		break			
	except:
		print("Debe introducir un número")

print(gcdIter(a,b))