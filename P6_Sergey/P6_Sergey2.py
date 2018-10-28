#!/usr/bin/python3

# Escriba​ ​un​ ​programa​ ​que​ ​pida​ ​un​ ​número​ ​y​ ​a​ ​continuación​ ​escriba​ ​
# la​ ​lista​ ​de​ ​todos​ ​los​ ​divisores del​ ​número​ ​(incluidos​ ​el​ ​uno​ ​y​ ​él​ ​mismo).

# 1-Inicialización de variables.
# 2-Pregunta e introducción de número.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero.
# 3-Operaciones necesarias para calcular los divisores.

#1#
lista = []
cont = 0

#2#
while True:
    try:
        numero = int(input("Dígame un número: "))
        break
    except ValueError:
        print("Debes introducir un número entero: ")

#3#
for i in range(1, numero+1):
    if numero % i == 0:
        lista.append(i)
        cont += 1
print("{} tiene {} divisores: {}".format(numero, cont, lista))
