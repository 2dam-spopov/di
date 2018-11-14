#num=0
#variableNum=-1
#while num>variableNum:
#	variableNum=num
#	num=int(input("Introduce número"))

#print("El número introducido", str(num), ", es menor que ", str(variableNum))


##################
#num=0
#variableNum=0

#while num>-1:
#	num=int(input("Introduce número"))
#	if num>0:
#		variableNum=variableNum+num
#print("Has introducido número negativo, la suma de todos los números positivos es = ", str(variableNum))


numero=int(input("Intro num"))
suma=0

while numero>0:
	suma=suma+numero
	numero=int(input("Introduce otro num"))

print("La suma de los num es: ", str(suma))	