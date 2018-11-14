class Miembro():
	# Definimos que parametros acepta el objeto "Miembro"
	def __init__(self, nombre, direccion, dni):
		self.nombre = nombre
		self.direccion = direccion
		self.dni = dni

	# Definimos un metodo toString() para que muestre todo el objeto ya parseado a string
	def toString(self):
		return "Nombre: " + self.nombre + ", Dirección: " + str(self.direccion) + ", DNI: " + str(self.dni)

# Definimos la clase hija "Profesor" que hereda de "Miembro"
class Profesor(Miembro):
	# Sobrecargamos el constructor de la super clase
	def __init__(self, nombre, direccion, dni, numRegistro):
		Miembro.__init__(self, nombre, direccion, dni)
		self.numRegistro = numRegistro

	# Definimos el método añadir asignatura que añade otro atributo al objeto
	def añadirAsignatura(self, object):
		self.asignatura.append(object.nombre)
		self.codigo = object.codigo

	# Definimos un metodo toString() para que muestre todo el objeto ya parseado a string
	def toStringSub(self):
		return self.toString() + ", Núm de registro: " + str(self.numRegistro)

# Definimos la clase hija "Estudiante" que hereda de "Miembro"
class Estudiante(Miembro):
	# Sobrecargamos el constructor de la super clase
	def __init__(self, nombre, direccion, dni, numEstudiante):
		Miembro.__init__(self, nombre, direccion, dni)
		self.numEstudiante = numEstudiante
		self.estudiantes = []

	# Definimos el método añadir profesor
	def añadirEstudiantes(self, object):
		self.estudiantes.append(object)

	# Mostramos todos los estudiantes agregados en la lista
	def imprimirEstudiantes(self):
		for indice in self.estudiantes:
			print(indice.toStringSub())

	# Definimos un metodo toString() para que muestre todo el objeto ya parseado a string
	def toStringSub(self):
		return self.toString() + ", Núm de estudiante: " + str(self.numEstudiante)

# Definimos la clase asignatura
class Asignatura:
	# Creamos el constructor
	def __init__(self, nombre, codigo):
		self.nombre = nombre
		self.codigo = codigo
		self.asignaturas = []

	# Imprimimos todas las asignaturas que estén en la lista Asginatura.asignaturas
	def imprimirAsignaturas(self):
		for indice in self.asignaturas:
			print(indice.toString())
	
	# Añadimos en la lista las diferentes asiganturas
	def guardarAsignatura(self, object):
		self.asignaturas.append(object)

	# Definimos un metodo toString() para que muestre todo el objeto ya parseado a string
	def toString(self):
		return "Nombre: " + self.nombre + ". Código: " + str(self.codigo)

# Instanciamos los objetos
Luis = Profesor("Luis", 50, 34567, 5001)
Luisito = Estudiante("Luisito", 20, 56678, 1001)
matematicas = Asignatura("Matematicas", 5)
algebra = Asignatura("Álgebra", 7)
matematicas.guardarAsignatura(matematicas)
matematicas.guardarAsignatura(algebra)
print("Profesores: ")
print(Luis.toStringSub())
print("Estudiante: ")
Luisito.añadirEstudiantes(Luisito)
Luisito.imprimirEstudiantes()
print("Asignaturas: ")
matematicas.imprimirAsignaturas()