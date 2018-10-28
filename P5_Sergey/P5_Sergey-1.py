#!/usr/bin/python3

# Escriba​ ​un​ ​programa​ ​que​ ​permita​ ​crear​ ​una​ ​lista​ ​de​ ​palabras.​ ​
# Para​ ​ello,​ ​el​ ​programa​ ​tiene​ ​que pedir​ ​un​ ​número​ ​y​ ​luego​ ​solicitar​ ​
# ese​ ​número​ ​de​ ​palabras​ ​para​ ​crear​ ​la​ ​lista.​ ​Por​ ​último,​ ​el
# programa​ ​tiene​ ​que​ ​escribir​ ​la​ ​lista.

# 1-Inicialización de variables. (He creado variables para los textos para probar)
# 2-Pregunta e introducción de número de palabras en la lista.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero mayor que 0 el programa sigue preguntando.
# 3-Creación de la lista con valores introducidos.

#1#
lista = []
pregNumero = "Dime cuántas palabras tiene la lista: "
resError = "Debes introducir un número entero mayor que 0"
intrPalabra = "Dígame la palabra {num}: "
listaCreada = "La lista creada es: "

#2#
while True:
    try:
        numPalabras = int(input(pregNumero))
        if numPalabras == 0 or numPalabras < 0:
            print(resError)
            continue
        break
    except ValueError:
        print(resError)

#3#
if numPalabras > 0:
    for i in range(0, numPalabras):
        palabra = input(intrPalabra.format(num=i+1))
        lista.append(palabra)
print(listaCreada, lista)
