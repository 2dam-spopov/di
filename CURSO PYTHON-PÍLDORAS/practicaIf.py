print("Programa de evaluacion de notas de alumnos")


notaAlumno=input()


def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspendido"	
	return valoracion
print(evaluacion(int(notaAlumno)))	