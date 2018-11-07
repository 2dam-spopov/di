#!/usr/bin/python3

# Importa funciones de otro archivo.
from funciones_p9 import *

lista=[]

print("\n__________________________________________________\n")
print("###### Introduce datos del triángulo! ############")
print("__________________________________________________\n")

while True:
	try:
		# Introduce por teclado datos del triángulo, permitiendo decimales.
		a = float(input("Introduce altura del triángulo:        "))
		b = float(input("Introduce base del triángulo:          "))

		print("\n__________________________________________________\n")
		print("###### Introduce datos de los segmentos! #########")
		print("__________________________________________________\n")

		# Introduce datos de los segmentos, controla excepciones en decimales y enteros.
		while True:
			try:
				num_segmentos=int(input("¿Cuántos segmentos introducirás?:      "))
				break
			except ValueError:
					print("Debes introducir un número entero!")	

		# Añade a la lista valores introducidos.
		while True:
			try:
				for i in range(0,num_segmentos):
					seg=float(input("Introduce el segmento {}:               ".format(i+1)))
					lista.append(seg)
				break
			except ValueError:
				print("Debes introducir un número!!!!!")		
		break

	except ValueError:
		print("Debes introducir un número!")

# Llama a las funciones pasando parámetros.
triangulo_area=area_triangulo(a,b)
suma_segmentos=longitud_seg(lista)

# Imprime resultados.
print("\n__________________________________________________\n")
print("###### Resultados ################################")
print("__________________________________________________\n")
print("El área del triángulo es:              {0:.2f}".format(triangulo_area))
print("La suma de los segmentos es:           {0:.2f}".format(suma_segmentos))
