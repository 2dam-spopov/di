#! /usr/bin/python3
def isVowel2(char):
	if len(char) > 1:
		print("Debe introducir solo un caracter, ha introducido {} caracteres".format(str(len(char))))
	if char.lower() in "aeiou":
		return True
	else:
		return False

string = input("Introduzca una letra: ")

print("Devuelve: " + str(isVowel2(string)))