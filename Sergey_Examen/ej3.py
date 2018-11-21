#!/usr/bin/python3


class Libro():
	"""
	Información acerca de un libro, incluye título, lista de autores,
	editorial, ISBN y precio.
	"""
	def __init__(self, titulo, autores, editor, isbn, precio):
		"""
			Construtor principal con parámetros por defecto.
		"""
		self.titulo = titulo
		self.autores = autores
		self.editor = editor
		self.isbn = isbn
		self.precio = precio

	def num_autores(self):
		"""
			Método que cuenta el número de autores del libro y devuelve dicho número.
		"""
		num=0
		for i in range(len(self.autores)):
			num+=1
		return num	
		
#Instanciamos el objeto e imprimimos los datos
python_libro = Libro("Practica1 Programming", ["Campbell", "Gries", "Montojo"], \
	"Pragmatic Bookshelf","978-1-93778-545-1", 25.0)

print("Datos del libro: ")
print(python_libro.titulo)
print(python_libro.autores)
print(python_libro.editor)
print(python_libro.isbn)
print(python_libro.precio)

print("\nNúmero de autores: ")
print(python_libro.num_autores())