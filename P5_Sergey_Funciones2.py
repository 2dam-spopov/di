#! /usr/bin/python3

def isVowel(char):
	if len(char) > 1:
		print("Debe introducir solo un caracter, ha introducido {} caracteres".format(str(len(char))))
	if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() =='o' or char.lower() == 'u':
		return True
	else:
		return False

letra = input("Introduzca una letra: ")	

print("Devuelve: " + str(isVowel(letra)))