#!/usr/bin/python3

# Escriba​ ​un​ ​programa​ ​que​ ​permita​ ​crear​ ​dos​ ​listas​ ​de​ ​palabras​ ​y​ ​que,​ ​a​ ​continuación,​ ​
# escriba​ ​las siguientes​ ​listas​ ​(en​ ​las​ ​que​ ​no​ ​debe​ ​haber​ ​repeticiones):
# ● Lista​ ​de​ ​palabras​ ​que​ ​aparecen​ ​en​ ​las​ ​dos​ ​listas.
# ● Lista​ ​de​ ​palabras​ ​que​ ​aparecen​ ​en​ ​la​ ​primera​ ​lista,​ ​pero​ ​no​ ​en​ ​la​ ​segunda.
# ● Lista​ ​de​ ​palabras​ ​que​ ​aparecen​ ​en​ ​la​ ​segunda​ ​lista,​ ​pero​ ​no​ ​en​ ​la​ ​primera.
# ● Lista​ ​de​ ​palabras​ ​que​ ​aparecen​ ​en​ ​ambas​ ​listas.

# 1-Inicialización de variables.
# 2-Pregunta e introducción de número de palabras en la lista.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero mayor que 0 el programa sigue preguntando.
# 3-Creación de la lista con valores introducidos.
# 4-Pregunta e introducción de número de palabras en la lista 2.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero mayor que 0 el programa sigue preguntando.
# 5-Creación de la lista 2 con valores introducidos.
# 6-Eliminación de valores repetidos de la lista 1.
# 7-Eliminación de valores repetidos de la lista 2.
# 8-Creación de listas que se piden.
# 9-Muestra resultado por pantalla.


#1#
lista = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []

#2#
while True:
    try:
        numPalabras = int(input("Dime cuántas palabras tiene la lista: "))
        if numPalabras == 0 or numPalabras < 0:
            print("Debes introducir un número mayor que 0")
            continue
        break
    except ValueError:
        print("Debes introducir un número entero")

#3#
if numPalabras > 0:
    for i in range(0, numPalabras):
        palabra = input("Dígame la palabra " + str(i+1) + ": ")
        lista.append(palabra)
print("La lista creada es: ", lista)

#4#
while True:
    try:
        numPalabras2 = int(input("Dime cuántas palabras tiene la lista 2: "))
        if numPalabras2 == 0 or numPalabras2 < 0:
            print("Debes introducir un número mayor que 0")
            continue
        break
    except ValueError:
        print("Debes introducir un número entero")

#5#
if numPalabras2 > 0:
    for i in range(0, numPalabras2):
        palabra2 = input("Dígame la palabra " + str(i+1) + ": ")
        lista2.append(palabra2)
print("La lista creada es: ", lista2)

#6#
listaInv = lista[::-1]
for i in range(len(lista)):
    palabraRep = listaInv.count(lista[i])
    if palabraRep > 1:
        listaInv.remove(lista[i])
lista = listaInv[::-1]

#7#
listaInv2 = lista2[::-1]
for i in range(len(lista2)):
    palabraRep2 = listaInv2.count(lista2[i])
    if palabraRep2 > 1:
        listaInv2.remove(lista2[i])
lista2 = listaInv2[::-1]


###Con dos bucles for (funciona)###
# for i in range(len(lista)):
#   for j in range(len(lista2)):
#        if lista[i]==lista2[j]:
#            lista3.append(lista[i])
#   if lista2.count(lista[i])==0:
#       lista4.append(lista[i])
#   if lista.count(lista2[i])==0:
#       lista5.append(lista2[i])

#8#
# Con un bucle for.
for i in range(len(lista)):
    if lista[i] in lista2:
        lista3.append(lista[i])
    if lista[i] not in lista2:
        lista4.append(lista[i])
    if lista2[i] not in lista:
        lista5.append(lista2[i])
lista6 = lista3+lista4+lista5

#9#
print("Palabras que aparecen en las dos listas: ", lista3)
print("Palabras que sólo aparecen en la primera lista: ", lista4)
print("Palabras que sólo aparecen en la segunda lista: ", lista5)
print("Todas las palabras: ", lista6)
