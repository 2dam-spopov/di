#!/usr/bin/python3

# Escriba​ ​un​ ​programa​ ​que​ ​permita​ ​crear​ ​una​ ​lista​ ​de​ ​palabras​ ​y​ ​que,​ ​
# a​ ​continuación,​ ​pida​ ​dos palabras​ ​y​ ​sustituya​ ​la​ ​primera​ ​por​ ​la​ ​segunda​ ​en​ ​la​ ​lista.

# 1-Inicialización de variables.
# 2-Pregunta e introducción de número de palabras en la lista.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero mayor que 0 el programa sigue preguntando.
# 3-Creación de la lista con valores introducidos.
# 4-Introducción de palabra a sustituir y la sustituta, si la palabra no está en la lista
#   da aviso y vuelve a pedir la introducción.

#1#
lista = []
flag = True

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
while flag:
    palabraSust = input("Sustituir la palabra: ")
    palabraNueva = input("por la palabra: ")
    vecesRepet = lista.count(palabraSust)
    if vecesRepet == 0:
        print("La palabra introducida no está en la lista, comprueba: ",
              lista, " y vuelve a intentarlo: ")
    else:
        flag = False
        for i in range(len(lista)):
            if lista[i] == palabraSust:
                lista[i] = palabraNueva
        print("La lista es ahora: ", lista)
