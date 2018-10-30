def longitud_seg(**segmentos):
	total = 0
	for i in segmentos:
		y=int(i)
		total += i
		return total
lista=[]
num=int(input("¿Cuántos segmentos introducirás?"))
for i in range(0,num):
	seg=int(input("Introduce los segmentos: "))
	lista.append(seg)
print(longitud_seg(tuple(lista)