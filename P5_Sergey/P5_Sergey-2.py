#!/usr/bin/python3

# Escriba​ ​un​ ​programa​ ​que​ ​permita​ ​crear​ ​una​ ​lista​ ​de​ ​palabras​ ​y​ ​que,​ ​
# a​ ​continuación,​ ​pida​ ​una palabra​ ​y​ ​diga​ ​cuántas​ ​veces​ ​aparece​ ​esa​ ​
# palabra​ ​en​ ​la​ ​lista.


# 1-Inicialización de variables.
# 2-Pregunta e introducción de número de palabras en la lista.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero mayor que 0 el programa sigue preguntando.
# 3-Creación de la lista con valores introducidos.
# 4-Pregunta palabra a buscar en la lista, dependiendo del resultado
#   la respuesta es distinta. Ofrece opción de buscar otra palabra
#   o finalizar el programa.

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
    palabraBuscar = input("Dígame la palabra a buscar: ")
    vecesRepet = lista.count(palabraBuscar)
    if vecesRepet == 1:
        print("La palabra: " + palabraBuscar + " aparece una vez en la lista.")
    elif vecesRepet == 0:
        print("La palabra: " + palabraBuscar + " no aparece en la lista.")
    else:
        print("La palabra: " + palabraBuscar + " aparece " +
              str(vecesRepet) + " veces en la lista.")
    if input("¿Desea buscar otra palabra? s/n ") != "s":
        flag = False
