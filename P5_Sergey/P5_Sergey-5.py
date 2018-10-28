#!/usr/bin/python3

# Escriba​ ​un​ ​programa​ ​que​ ​permita​ ​crear​ ​dos​ ​listas​ ​de​ ​palabras​ ​y​ ​que,​ ​
# a​ ​continuación,​ ​elimine​ ​de la​ ​primera​ ​lista​ ​los​ ​nombres​ ​de​ ​la​ ​segunda​ ​lista.

# 1-Inicialización de variables.
# 2-Pregunta e introducción de número de palabras en la lista.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero mayor que 0 el programa sigue preguntando.
# 3-Creación de la lista con valores introducidos.
# 4-Pregunta e introducción de número de palabras en la lista 2.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero mayor que 0 el programa sigue preguntando.
# 5-Creación de la lista 2 con valores introducidos.
# 6-Control de excepción cuándo la palabra de la lista 2 no aparece
#   en la lista 1. En caso positivo se eliminan las palabras de la
#   lista 1.

#1#
lista = []
lista2 = []

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
try:
    for i in range(len(lista2)):
        palabraElim = lista2[i]
        lista.remove(palabraElim)
    print("La lista ahora es: ", lista)
except ValueError:
    print("Las palabras a eliminar no se encuentran en la lista 1")
