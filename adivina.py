#!/usr/bin/python3

import random

def adivina():
	"""
	Crea un número aleatorio y lo compara con el número introducido 
	por teclado. Dependiendo del resultado de la comparación nos sale
	un mensaje.
	Si se introduce un caracter distinto a un entero sale mensaje de aviso.
	"""
	print("***ADIVINA NÚMERO***")
	aleatorio=random.randint(0,11)
	numero=0
	while numero!= aleatorio:
		numero=int(input("\nIntroduce un número: "))
		if aleatorio > numero:
			print("Debes introducir un número mayor")
		elif aleatorio < numero:
			print("Debes un número menor")	
		else:
			print("Has acertado, el número es", aleatorio)
try:			
	adivina()
except:
	print("Debes introducir números enteros.")	