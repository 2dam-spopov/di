miDiccionario={"Alemania":"Berlin","Francia":"Paris", "Reino Unido":"Londres", "Espana":"Madrid"}
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)
#Soobreescribe el anterior valor, solo puede haber una clave
miDiccionario["Italia"]="Roma" 
print(miDiccionario)
#Borra una clave
del miDiccionario["Reino Unido"]
print(miDiccionario)

#A la posicion de un clave en una tupla asignamos su valor
miTupla=("Espana", "Francia", "Reino Unido", "Alemania")
miDiccionario2={miTupla[0]:"Madrid", miTupla[1]:"Paris"}
print(miDiccionario2) 

#miTuplaAnios=(1991,1992,1993,1997,1998)
#miDiccionarioAnios={"temporadas":(1991,1992,1993,1997,1998)}
#Diccionario dentro de otro diccionario
miDiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1997,1998]}}
print(miDiccionario3)
#Imprime las claves
print(miDiccionario3.keys())
#Imprime los valores
print(miDiccionario3.values()) 
#Imprime la longitud del diccionario
print(len(miDiccionario3)) 
