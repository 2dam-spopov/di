class Persona():
	def __init__(self, edad, nombre):  
		self.edad = edad
		self.nombre = nombre

	def cumpleaños(self):
		self.edad+= 1
luis = Persona(31, "Luis")
print(luis.edad,luis.nombre)
luis.cumpleaños()
print("Despues del cumpleaños:", luis.edad)