#! /usr/bin/python3

def comparar(varA, varB):
	"""
	varA: Valor introducido por teclado.
	varB: Valor intorducido por teclado.
	devuelve: si el varA es mayor, menor, igual a varB o si ha cadena involucrada.
	"""
	if varA.isdigit() and varB.isdigit():
		if varA > varB:
			return "Grande"
		elif varA == varB:
			return "Igual"
		elif varA < varB:
			return "Más pequeño"
	else:
		return("Cadena involucrada")

varA = input("Introduzca varA: ")
varB = input("Introduzca varB: ")

print(comparar(varA, varB))

	