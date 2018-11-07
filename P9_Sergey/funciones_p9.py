#!/usr/bin/python3

def area_triangulo(a,b):
	"""Calcula área de un triángulo"""
	area=(a*b)/2
	return area

def longitud_seg(lista):
	"""Suma longitud de número variable de segmentos"""
	total = 0
	for i in range(len(lista)):
		total+=lista[i]
	return total
