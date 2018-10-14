#!/usr/bin/python3

contRepet = 0
palabras = 0
lista = []
intro = ""
palabraBuscar = ""
flag = "s"

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

while flag == "s":
    palabraBuscar = input("Dígame la palabra a buscar: ")
    contRepet = lista.count(palabraBuscar)
    if contRepet == 1:
        print("La palabra: " + palabraBuscar + " aparece una vez en la lista.")
    elif contRepet == 0:
        print("La palabra: " + palabraBuscar + " no aparece en la lista.")
    else:
        print("La palabra: " + palabraBuscar + " aparece " +
              str(contRepet) + " veces en la lista.")

    flag = input("¿Desea buscar otra palabra? s/n ")
