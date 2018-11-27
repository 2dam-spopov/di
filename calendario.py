import calendar
import locale

def dia_semana(año,mes,dia):
	"""
		Función que recibe parámetros día, mes, año.
		Devuelve el día de la semana.
		Controla excepción de formato de fecha.
	"""
	try:
		locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
		dia_semana = calendar.day_name[calendar.weekday(año,mes,dia)]
		print("El día de la semana de {}/{}/{} es {}!".format(dia,mes,año,dia_semana))
	except:
		print("El formato de fecha está fuera de rango!")	

#Introduce día, mes, año por teclado.
#Controla excepción de tipo.
while True:
	try:
		dia=int(input("Introduce día: "))
		mes=int(input("Introduce mes: "))
		año=int(input("Introduce año: "))
		break
	except:
		print("Debes introducir fecha en este formato dd/mm/aaaa.")	

#Llamada a la función.
dia_semana(año,mes,dia)