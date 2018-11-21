#!/usr/bin/python3

def mismo_primero_ultimo(lista):
	"""
	Función que recibe como parámetro una lista.
	Asignamos a la variable primero el valor de la primera posición.
	Invertimos la lista y asignamos a la variable ultimo el valor de
		la priemra posición.
	Comparamos ambos valores.
	Si variable primero y ultimo son iguales devuelve True, en 
	caso contrario False.	
	"""
	primero=lista[0]
	listaInv = lista[::-1]
	ultimo=listaInv[0]
	if primero == ultimo:
		return True
	else:
		return False	

#Creamos una lista vacía.
lista = []

#Guardamos en una variable el número de ítems que vamos a introducir.
#Controlamos que debe ser un número entero mayor que 2.
flag = True
while True:
	try:
		while flag:
			num_items=int(input("¿Cuántos ítems vas a introducir?"))

			#Precondición, deben de haber al menos 2 ítems en la lista.
			#Si la condición se cumple añade ítems a la lista, en caso contrario
			#mensaje de aviso.
			if num_items>=2:
				for i in range(0,num_items):
					items=input("Introduce el ítem {}:".format(i+1))
					lista.append(items)

				#Llamamos a la función e imprimimos lo que devuelve.
				print(mismo_primero_ultimo(lista))
				flag=False
			else:
				print("Debes introducir 2 o más ítems.")
		break
	except ValueError:
		print("Debes introducir un número entero")	
