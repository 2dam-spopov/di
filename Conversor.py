#!/usr/bin/python3

# El ejercicio trata de introducir por teclado un número en base 2 y mostrarlo por pantalla en base 10.

# 1-Asignación a la variable numero el valor introducido por teclado.
# 2-Inversión de la cadena introducida para los calculos.
# 3-Inicialización de variables necesarias para los calculos.
# 4-Comprobación de número binario recorriendo la cadena. Si no es binario impresión de aviso.
# 5-Realización de calculos necesarios e impresión por pantalla del resutado.


#1#
numero = input("Introduce número en binario")

#2#
numeroInver = numero[::-1]

#3#
contador = -1
resulFinal = 0
resulOperacion = 0
flag = True

#4#
for i in range(len(numeroInver)):
    if flag == True:
        if numero[i] != "1" and numero[i] != "0":
            print("El número no es binario")
            flag = False

#5#
if flag == True:
    for j in range(len(numeroInver)):
        contador += 1
        if numero[j] == "1":
            resulOperacion = 2**contador
            resulFinal += resulOperacion
    print(resulFinal)
