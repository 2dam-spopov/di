#!/usr/bin/python3

# Escriba​ ​un​ ​programa​ ​que​ ​calcule​ ​términos​ ​de​ ​la​ ​sucesión​ ​
# Un​ +1​​ ​=​ ​3​ ​U​n​​ ​+​ ​1​ ​si​ ​U​n​​ ​es​ ​impar​ ​y​ ​U​ ​​n+1​​ ​= U​n​​ ​/​ ​2​ ​si​ ​U​n​​ ​es​ ​par.​ ​
# El​ ​programa​ ​tiene​ ​que​ ​pedir​ ​el​ ​término​ ​U​0​​ ​y​ ​el​ ​número​ ​de​ ​términos​ ​a​ ​calcular.
# Cálculo​ ​de​ ​términos​ ​de​ ​la​ ​sucesión​ ​U(n+1)=3.U(n)+1​ ​si​ ​n​ ​es​ ​impar​ ​y​ ​
# U(n)=U(n)/2​ ​si​ ​n​ ​es​ ​par.



# Pregunta e introducción de número. Se usa control de error de excepción,
#    si no se entroduce un número entero.
while True:
    try:
        u = int(input("Introduce valor de U(0): "))
        term = int(input("Dime cuántos términos quieres: "))
        break
    except ValueError:
        print("Debes introducir números enteros")

# Inicialización de una lista.
lista = [u]        

# Calcula la sucesión y muestra la lista.
for i in range(1, term):
    if u % 2 != 0:
        resul = (3*u)+1
        u = resul
        lista.append(resul)
    else:
        resul = int(u/2)
        u = resul
        lista.append(resul)
print(lista)
