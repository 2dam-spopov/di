#! /usr/bin/python3
def comparador(varA, varB):
		if varA > varB:
			print("Grande")
		elif varA == varB:
			print("Igual")
		elif varA < varB:
			print("Más pequeño")

try:
	varA = int(input("Introduzca varA: "))
	varB = int(input("Introduzca varB: "))
	comparador(varA, varB)
except:
	print("Cadena involucrada")