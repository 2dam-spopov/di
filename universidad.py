#! /usr/bin/python3

class Miembro():
	"""
		Clase superior.
	"""

	def __init__(self, nombre, edad, dni):
		"""
			Construtor principal con parámetros por defecto.
		"""
		self.nombre = nombre
		self.edad = edad
		self.dni = dni

	def docencia(self):
		"""
			Método que imprime los parámetros por defecto.
		"""
		print("Nombre: ", self.nombre, " Edad: ",
			self.edad, " DNI: ", self.dni, end="")


class Profesor(Miembro):
	"""
		Clase profesor que hereda de la clase super Miembro.
	"""
	def __init__(self, nombre_profesor, edad_profesor, dni_profesor, registro):
		"""
			Método que espera parámetros de la clase super y sus propios parámetros.
		"""
		super().__init__(nombre_profesor, edad_profesor, dni_profesor)
		self.registro = registro

	def docencia(self):
		"""
			Método que invoca la método docencia de la clase super con los parámetros por defecto
			e imprime su propio parámetro.
		"""
		super().docencia()
		print(" NºReg.: ", self.registro)


class Estudiante(Miembro):
	"""	Clase estudiante que hereda de la clase super Miembro.
	"""
	def __init__(self, nombre_estudiante, edad_estudiante, dni_estudiante, numero):
		super().__init__(nombre_estudiante, edad_estudiante, dni_estudiante)
		self.numero = numero
		"""Método que espera parámetros de la clase super y sus propios parámetros.
		"""
	def docencia(self):
		"""Método que invoca la método docencia de la clase super con los parámetros por defecto
			e imprime su propio parámetro.
		"""
		super().docencia()
		print(" NºEst.: ", self.numero)


class Asignatura():
	"""
		Clase asignatura con sus propios métodos.
	"""
	def __init__(self, nombre_asignatura, codigo):
		"""
			Constructor con parámetros por defecto.
		"""
		self.nombre_asignatura = nombre_asignatura
		self.codigo = codigo
	def asignaturas(self):    
		"""
			Método que imprime los parámetros pasados.
		"""
		print("Nombre: ", self.nombre_asignatura +
				" CódAsignat.:", self.codigo)


luis = Profesor("Luis", 50, "1231243F", 5001)
print("\nProfesor: ")
luis.docencia()

luisito = Estudiante("Luisito", 20, "1233423J", 6002)
print("\nEstudiante: ")
luisito.docencia()

algebra = Asignatura("Algebra", 7)
mates = Asignatura("Matemáticas", 5)
print("\nAsignaturas: ")
algebra.asignaturas()
mates.asignaturas()
