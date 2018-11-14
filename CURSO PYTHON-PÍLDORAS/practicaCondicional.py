salarioPresidente=int(input("Introduce salario presidente: "))
print("salario Presidente: " + str(salarioPresidente))

salarioDirector=int(input("Introduce salario director: "))
print("salario Director: " + str(salarioDirector))

salarioJefe=int(input("Introduce salario jefe: "))
print("salario Jefe: " + str(salarioJefe))

salarioAdmin=int(input("Introduce salario Admin: "))
print("salario Admin: " + str(salarioAdmin))

if salarioAdmin<salarioJefe<salarioDirector<salarioPresidente:
	print("Todo esta bien")
else:
	print("Algo va mal")