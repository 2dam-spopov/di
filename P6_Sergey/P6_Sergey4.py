#!/usr/bin/python3

# Pregunta e introducción de número. Se usa control de error de excepción,
#    si no se entroduce un número entero.
while True:
    try:
        a = int(input("Introduce valor de a: "))
        b = int(input("Introduce valor de b: "))
        u = int(input("Introduce valor de U(0): "))
        term = int(input("Dime cuántos términos quieres: "))
        break
    except ValueError:
        print("Debes introducir números enteros")


# Inicialización de una lista.
lista = [u]

# Calcula la sucesión y muestra la lista.
for i in range(1, term):
    resul = (a*u)+b
    u = resul
    lista.append(resul)
print(lista)
