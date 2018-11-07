#! /usr/bin/python3

def isVowel(char):
	"""
	char: letra introducida por teclado.
	devuelve: verdadero si char es vocal, falso en caso contrario.
	"""
	if len(char) > 1:
		print("Debe introducir solo un caracter, ha introducido {} caracteres".format(len(char)))
	vocal = char.lower()
	if vocal  == 'a' or vocal  == 'e' or vocal  == 'i' or vocal  =='o' or vocal  == 'u':
		return True
	else:
		return False

letra = input("Introduzca una letra: ")	

print("Devuelve: ", isVowel(letra))