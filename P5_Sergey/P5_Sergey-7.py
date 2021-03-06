#!/usr/bin/python3

# Escriba​ ​un​ ​programa​ ​que​ ​permita​ ​crear​ ​una​ ​lista​ ​de​ ​palabras​ ​y​ ​que,​ ​
# a​ ​continuación,​ ​elimine​ ​los elementos​ ​repetidos​ ​(dejando​ ​únicamente​ ​
# el​ ​primero​ ​de​ ​los​ ​elementos​ ​repetidos).

# 1-Inicialización de variables.
# 2-Pregunta e introducción de número de palabras en la lista.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero mayor que 0 el programa sigue preguntando.
# 3-Creación de la lista con valores introducidos.
# 4-Inversión de la lista y guardada en lista 2 para eliminar todas
#   las palabras iguales menos la primera (remove() borra de derecha a izquierda).
#   Se invierte la lista 2 y se guarda en lista.

#1#
lista = []

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
lista2 = lista[::-1]

for i in range(len(lista)):
    palabraRep = lista2.count(lista[i])
    if palabraRep > 1:
        lista2.remove(lista[i])
lista = lista2[::-1]
print("La lista sin repeticiones es: ", lista)            


