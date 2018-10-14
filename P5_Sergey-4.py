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
    palabraBorr = input("Palabra a eliminar: ")
    contRepet = lista.count(palabraBorr)
    if contRepet == 0:
        print("La palabra introducida no está en la lista, comprueba: ",lista," y vuelve a intentarlo: ")
    else:
        flag = False
        for i in range(contRepet):
            lista.remove(palabraBorr)
        print("La lista es ahora: ", lista)
        flag2=input("¿Desea borrar otra palabra? s/n")
        if flag2=="s":
            flag==True

