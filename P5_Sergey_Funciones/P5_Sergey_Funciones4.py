#! /usr/bin/python3

def isVowel(char):
	vocales = 0
	for i in char:
		if i.lower() in "aeiou":
			vocales += 1
	return vocales

s = input("Introduzca una palabra: ")
print("Número de vocales: ", isVowel(s))