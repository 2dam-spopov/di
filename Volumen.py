class Volumen():
	def __init__(self):
		self.nivel = 3
		print('nivel', self.nivel)
	def subir(self):
		self.nivel += 1
		if self.nivel > 10:
			self.nivel = 10
		print('nivel', self.nivel)
	def bajar(self):
		self.nivel -= 1
		if self.nivel < 0:
			self.nivel = 0 
		print('nivel', self.nivel)
	def silenciar(self):
		self.nivel = 0
		print('nivel', self.nivel)

#controlVolumen = Volumen() 
#controlVolumen.subir()  
#controlVolumen.subir()
#controlVolumen.bajar()
#controlVolumen.silenciar() 
#controlVolumen.bajar()


class Graves(Volumen):
	'''se crea la clase graves a partir de clase volumen'''
	pass
control_graves = Graves()
control_graves.subir()

class Volumen_velocidad(Volumen):
	def __init__(self, velocidad):
		if velocidad > 120:
			self.nivel = 5
		elif velocidad > 100:
			self.nivel = 4
		else:
			self.nivel = 3
		print("nivel",self.nivel)
control_volumen_velocidad = Volumen_velocidad(110)
control_volumen_velocidad.subir()