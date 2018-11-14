#! /usr/bin/python3

class Pais():

	def __init__(self, nombre, poblacion, area):
		""" 
			Constructor por defecto con los parámetros que se le pasan al instanciar la clase.
		"""
		self.nombre=nombre
		self.poblacion=poblacion
		self.area=area

	def mas_grande_que(self,pais_2):
		""" 
			Comprueba si el área del primer país es más grande devolviendo true o false.
		"""
		return self.area > pais_2.area

	def densidad_de_poblacion(self):
		"""
			Hace el cálculo de la densidad de población y devuelve el resultado
		"""
		return self.poblacion/self.area	

francia=Pais("Francia",66030000, 640679)
españa=Pais("España",46770000, 504645)

francia.mas_grande_que(españa)
españa.mas_grande_que(francia)

print("------------------------------------------------------------------------")
print("{0} es más grande que {1}: {2}".format(españa.nombre, francia.nombre, españa.mas_grande_que(francia)))
print("{0} es más grande que {1}: {2}".format(francia.nombre, españa.nombre, francia.mas_grande_que(españa)))
print("------------------------------------------------------------------------")
print("La densidad de población de {0} es de: {1} habitantes por km2".format(españa.nombre,"{0:.2f}".format(españa.densidad_de_poblacion())))
print("La densidad de población de {0} es de: {1} habitantes por km2".format(francia.nombre,"{0:.2f}".format(francia.densidad_de_poblacion())))
print("------------------------------------------------------------------------")

