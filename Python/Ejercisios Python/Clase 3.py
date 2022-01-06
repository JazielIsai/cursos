#Listas:
#Es una estructura de datos que nos permite almacenar gran cantidad de valores (equivalente a los array en otros lenguajes)
#En python las listas pueden guardar diferentes tipos de valores 
#Se puede expandir dinámicamente añadiendo nuevos elementos 
#Sintaxis 
#Nombre de la lista:
#nombrelista=[elem1,elem2,elem3...]

milista=['Maria','Pepe','Martha','Antonio']

milista.append('Sandra') #Agrega un elemento al final de la lista

milista.insert(2,'Samantha') #Agrega una persona a la lista, pidiendo 2 argumento uno(2) en la posicion que quiere que lo agregemos y luego a el elemento 

milista.extend(['ana','lupita'])#Agregamos a la lista, mas elementos

print(milista.index("Samantha"))#Muestra en que posicion esta el elemento

print(milista[:]) #Imprimir toda la lista
print(milista[3]) #Imprimir por posicion  

print(milista[0:2])#Imprimi una parte o porcion de la lista ya establecida

print(milista[2:]) #Hacede a los ultimos eelementos

print('Pepe'in milista) #Esta imprimiendo un elemnto si(in) se encuentra en (milista) el elemnto

#Inicio otra lista

misegundalista=['Perla', 5, True, 21.1]

misegundalista.remove('Perla')  #Eliminacion de elemntos de una lista asigana entre () el elemnto que deseas eliminar 

misegundalista.pop()#Elimina el ultimo elemento de una lista

print(misegundalista[:])


#Sumar listas

milista1=['Chata', 'Chato']
milista2=[4,78.3]
milista3=milista1+milista2
print(milista3[:])

#Repetidor de listas
milsta4=['Juan', 'Pancho', 2, True ] * 2 #El (* 2) marca las veces en el cual se repitira la lista
print(milsta4[:])