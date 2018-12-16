
#!/usr/bin/python3

import turtle


"""
Devuelve un objeto singleton de la subclase TurtleScreen.
Es una herramienta que se usa parahacer gráficos.
"""
window = turtle.Screen()

cursor = turtle.Turtle()
#Gira a la izquierda
cursor.left(90)
#Sigue recto
cursor.forward(90)
#Gira a la derecha
cursor.right(90)

for x in range(1,25):
	"""
	Repite los siguientes movimientos en el rango de 1 y 25.
	"""
	cursor.left(5)
	cursor.forward(45)
	cursor.left(100)
	cursor.forward(45)
#Cierra la ventana cuando finaliza al hacer click	
window.exitonclick()