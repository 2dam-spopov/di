#!/usr/bin/python3


lista = []
lista2 = []
intro = ""
flag = True

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

    for i in range(0, palabras):
        intro = input("Dígame la palabra " + str(i+1) + ": ")
        lista.append(intro)

    print("La lista creada es: ", lista)





while True:
    try:
        palabras2 = int(input("Dime cuántas palabras a eleminar tiene la lista: "))
        if palabras2 == 0 or palabras2 < 0:
            print("Debes introducir un número mayor que 0")
            continue
        break
    except ValueError:
        print("Debes introducir un número entero")

if palabras2 > 0:

    for i in range(0, palabras2):
        intro2 = input("Dígame la palabra " + str(i+1) + ": ")
        lista2.append(intro2)

    print("La lista de palabras a eleminar es: ", lista2)


try:
    for i in range(len(lista2)):
        palabraBorr=lista2[i]
        lista.remove(palabraBorr)
    print("La lista ahora es: ",lista)  
except ValueError:
    print("La palabras a eleminar no se encuentran en la lista")