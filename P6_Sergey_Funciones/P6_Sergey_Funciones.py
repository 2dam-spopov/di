#! /usr/bin/python3
def iterPower(base, exp):
	'''
	base: número entero o decimal.
	exp: exponente número mayor que 0.
	devuelve: el resultado de la operación.

	'''
	resultado = base
	for i in range(1, exp):
		resultado *= base
	return resultado


while True:
	try:
		base = float(input("Introduzca la base: "))
		break			
	except:
		print("Debe introducir un número")

while True:
	try:
		exp = int(input("introduca el exponente: "))
		if exp < 0:
			exp = int("error")
		break
	except:	
		print("Debes introducir un número mayor que 0")	

print("El resultado es: ", iterPower(base, exp))
