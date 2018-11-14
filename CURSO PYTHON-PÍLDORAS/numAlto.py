
def DevuelveMax(num1, num2):
	valor="es menor"
	if num1>num2:
		valor="es mayor"
		return valor
	else:
		return valor

nume1=int(input("Introduce primer numero: "))
nume2=int(input("Introduce segundo numero: "))

print("El ",nume1, DevuelveMax(nume1,nume2)," que ",nume2)