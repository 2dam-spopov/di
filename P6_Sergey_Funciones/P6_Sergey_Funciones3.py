#! /usr/bin/python3

def cadena(s,s2):
	"""
	s: cadena principal introducida por teclado.
	s2: subcadena o cadena a buscar en s.
	devuelve: las veces que se repite s2 en s.
	"""
	return s.count(s2)

s = input("Introduzca la cadena: ")
s2 = input("Introduzca cadena a buscar: ")

print("Numero de veces que ocurre es: ", cadena(s,s2))

