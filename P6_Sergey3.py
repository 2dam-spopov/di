#!/usr/bin/python3
# Escriba​ ​un​ ​programa​ ​que​ ​pida​ ​un​ ​número​ ​y​ ​a​ ​continuación​ ​
# escriba​ ​la​ ​lista​ ​de​ ​todos​ ​los​ ​números primos​ ​hasta​ ​él..

# 1-Inicialización de variables.
# 2-Pregunta e introducción de número.
#   Se usa control de error de excepción, si no se entroduce un
#   número entero.
# 3-Operaciones necesarias para calcular los números primos, si el número
#   es primo se añade a una lista que despues se muestra.

#1#
primo = True
lista=[]

#2#
while True:
    try:
        num = int(input("Dígame un número"))
        break
    except ValueError:
        print("Debes introducir un número entero")

#3#
for i in range(1,num+1):
	for j in range(2,i):
		if i % j ==0:
			primo=False
	if primo ==True:
		lista.append(i)
	primo = True
print(lista)