#!/usr/bin/python3


lista = []
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


while flag==True:
    palabraSust = input("Sustituir la palabra: ")
    palabraNueva = input("por la palabra: ")
    contRepet = lista.count(palabraSust)
    if contRepet == 0:
        print("La palabra introducida no está en la lista, comprueba: ",lista," y vuelve a intentarlo: ")
    else:
        flag = False
        for i in range(len(lista)):
            if lista[i] == palabraSust:
                lista[i] = palabraNueva
        print("La lista es ahora: ", lista)
