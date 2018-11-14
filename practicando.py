class Persona():
	def __init__(self, nombre, edad):
		self.nombre=nombre;
		self.edad=edad;
	def obtener_nombre(self):
		return self.nombre

	def obtener_edad(self):
		return self.edad

class Alumno(Persona):
	def __init__(self, nombre,edad,nota):
		Persona.__init__(self,nombre,edad)	
		self.nota=nota
	def obtener_nota(self):
		a=super().obtener_nombre()
		b=super().obtener_edad()
		print(a,b,self.nota)
		
alumno=Alumno("Sergio",27,9)
alumno.obtener_nombre()
alumno.obtener_edad()	
alumno.obtener_nota()

persona=Persona("Jose",14)
print(persona.nombre)

class Persona():
	def __init__(self, nombre, edad):
		self.nombre=nombre;
		self.edad=edad;
	def obtener_nombre(self):
		print(self.nombre)

	def obtener_edad(self):
		print(self.edad)

class Alumno(Persona):
	def __init__(self, nombre,edad,nota):
		super().__init__(nombre,edad)	
		self.nota=nota
	def obtener_nota(self):
		super().obtener_nombre()
		super().obtener_edad()
		print(self.nota)

alumno=Alumno("Sergio",27,9)
alumno.obtener_nombre()
alumno.obtener_edad()	
alumno.obtener_nota()
