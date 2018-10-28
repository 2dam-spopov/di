def longitud_seg(lista):
	"""Suma longitud de número variable de segmentos"""
	total = 0
	for i in range(len(lista)):
		total+=lista[i]
	return total

lista=[]
while True:
	try:
		num=int(input("¿Cuántos segmentos introducirás?"))
		for i in range(0,num):
			seg=int(input("Introduce los segmentos: "))
			lista.append(seg)
		break	
	except ValueError:
		print("Debes introducir un número!")
print(longitud_seg(lista))		
