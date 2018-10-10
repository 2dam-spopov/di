#!/usr/bin/python3

while True:
	try:
		palabras = int(input("Dime cuántas palabras tiene la lista: "))
		break
	except ValueError:
		print("Debes introducir un número entero")	

if palabras > 0:
	lista=[]
	for i in range(0, palabras):
		intro = input("Dígame la palabra "+ str(i+1)+ ": ")
		lista.append(intro)

	print("La lista creada es: ",lista)	
else:
	print("Imposible con 0 palabras")
