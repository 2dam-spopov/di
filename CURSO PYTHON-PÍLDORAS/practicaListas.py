miLista=["juan", "Jose", "Maria", "Antonio"]
#Anade al final
miLista.append("Sandra") 
#Inserta en la posicion deseada
miLista.insert(2,"Julia") 
#Anade varios al final
miLista.extend(["Ana", "Carlos"]) 
#Imprime toda la lista
print(miLista[:]) 
#Borra la poscion deseada
miLista.remove(miLista[2]) 
#Borra el ultimo
miLista.pop()
print(miLista[:])
#Muestra la posicion de un elemento
print(miLista.index("Maria")) 
#Confirma si esta o no en la lista
print("Antonio" in miLista) 

miLista2=["Kento","Marhuenda"]

miLista3=miLista+miLista2
print(miLista3[:])

#Cuenta las veces que esta lo que buscamos
print(miLista.count("Maria")) 
#Dice cuantos elementos hay en la lista
print(len(miLista3)) 