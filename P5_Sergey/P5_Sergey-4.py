#!/usr/bin/python3

# Escriba​ ​un​ ​programa​ ​que​ ​permita​ ​crear​ ​una​ ​lista​ ​de​ ​palabras​ ​y​ ​que,​ ​
# a​ ​continuación,​ ​pida​ ​una palabra​ ​y​ ​elimine​ ​esa​ ​palabra​ ​de​ ​la​ ​lista.


# 1-Inicialización de variables.
# 2-Pregunta e introducción de número de palabras en la lista.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero mayor que 0 el programa sigue preguntando.
# 3-Creación de la lista con valores introducidos.
# 4-Introducción de palabra para eliminación. Si la palabra no está en
#   la lista da aviso y vuelve a preguntar. Da posibilidad de borrar
#   otra palabra o terminar el programa.

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
    palabraElim = input("Palabra a eliminar: ")
    vecesRepet = lista.count(palabraElim)
    if vecesRepet == 0:
        print("La palabra introducida no está en la lista, comprueba: ",
              lista, " y vuelve a intentarlo: ")
    else:
        for i in range(vecesRepet):
            lista.remove(palabraElim)
        print("La lista es ahora: ", lista)
        if input("¿Desea borrar otra palabra? s/n") != "s":
            flag = False
