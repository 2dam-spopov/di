#!/usr/bin/python3

palabras = 0
while True:
    try:
        palabras = int(input("Dime cuántas palabras tiene la lista: "))
        if palabras == 0 or palabras < 0:
            print("Debes introducir un número mayor que 0")
            continue
        break
    except ValueError:
        print("Debes introducir un número entero")

if palabras > 0:
    lista = []
    for i in range(0, palabras):
        intro = input("Dígame la palabra " + str(i+1) + ": ")
        lista.append(intro)

    print("La lista creada es: ", lista)
