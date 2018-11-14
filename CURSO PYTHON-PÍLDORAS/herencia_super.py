class Persona():
	def __init__(self, nombre, edad, residencia):
		self.nombre=nombre
		self.edad=edad
		self.residencia=residencia
	def descripcion(self):
		print("nombre: ", self.nombre, "edad: ", self.edad, "residencia: ", self.residencia)


class Empleado(Persona):
	def __init__(self, salario, antigüedad,nombre_empleado,edad_empleado, residencia_empleado):
		super().__init__(nombre_empleado,edad_empleado, residencia_empleado)
		self. salario=salario
		self.antigüedad=antigüedad

	def descripcion(self):
		super().descripcion()
		print("Salario: ",self.salario, "antigüedad: ", self.antigüedad)

manu=Empleado(1500,15,"Manu", 45, "Chile")
manu.descripcion()

print(isinstance(manu,Persona))
						