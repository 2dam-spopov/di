
def mismo_primero_ultimo(lista):
	primero=lista[0]
	listaInv = lista[::-1]
	ultimo=listaInv[0]
	if primero == ultimo:
		return True
	else:
		return False	

lista = []

num_items=int(input("¿Cuántos ítems vas a introducir?"))

if num_items>=2:
	for i in range(0,num_items):
		items=input("Introduce el ítem {}:".format(i+1))
		lista.append(items)
else:
	print("Debes introducir 2 o más ítems!!")


print(mismo_primero_ultimo(lista))