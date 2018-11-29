#!/usr/bin/python3

def divisores(numero):
	"""
	Método al cuál pasamos por parámetro un número introducido por teclado
	y calculamos sus divisores. Si el número introducido no es un entero sale 
	mensaje de aviso.
	"""
	print("Divisores: ")
	for i in range(1,numero+1):
		if numero%i==0:
			print(i)


try:
	numero=int(input("Introduce un número: "))
	divisores(numero)
except:
	print("Debes introducir un número entero")	