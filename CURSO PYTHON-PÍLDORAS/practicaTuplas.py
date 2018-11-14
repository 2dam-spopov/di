#Conveirte de tupla a lista (Diferencia en parentesis y corchete)
miTupla=("Sergio",13,1,1991)
miLista=list(miTupla)
print(miLista)
print(miTupla)

#Convierte de lista a tupla
miLista2=["Sergio",13,1,1991]
miTupla2=tuple(miLista2)
print(miLista2)
print(miTupla2)

print(miTupla.count(13))
print(len(miTupla))

#Desempaquetado de tupla
nombre, dia, mes, agno=miTupla;
print(dia)