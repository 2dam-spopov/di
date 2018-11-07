#! /usr/bin/python3

def item_order(orden):
	"""
	orden: productos que se introducen para la orden.
	devuelve: el número de cada producto que se ha introducido en la orden.
	"""
	agua= orden.count("agua")
	hamburguesa= orden.count("hamburguesa")
	ensalada= orden.count("ensalada")

	return "agua: {0} Hamburguesa: {1} ensalada: {2} ".format(agua, hamburguesa, ensalada) 

orden = input("Introduzca su orden: ")

print(item_order(orden))