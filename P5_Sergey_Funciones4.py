#! /usr/bin/python3
string = input("Introduzca una palabra para ver cuantas vocales tiene: ")
# Definimos la función
def isVowel(char):
	vocal = 0
	# Iniciamos el ciclo
	for c in char:
		# Buscamos si el caracter coincide con alguna vocal
		if c in "aeiouAEIOU":
			vocal = vocal + 1
	# Devolvemos el número de vocales que hay en el parametro
	return vocal
# Imprimimos el resultado
print("Tiene: " + str(isVowel(string)) + " vocal/es")