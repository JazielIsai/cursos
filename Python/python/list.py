#List are also ordered sequences -> Las listas tambien son una secuencia ordenada
#A list is respresented with square brackets -->  Una lista se representa con corchetes
#List mutable -> Una lista es mutable 
# Las listas pueden contener cadenas, flotantes, enteros y aun podemos anidadr otras listas.
# Tambien en las listas podemos anidar tuplas y otras estructuras de datos

Lista = [ "Michel Jackson", 10.1, 1982 ]

# Para acceder a los elementos de la lista se puede hacer por medio de su indece, partiendo desde el cero
Lista[0] # Michel Jackson
Lista[1] # 10.1
Lista[2] # 1982

#Tambien se puede rebanar una lista
Lista0 = [ "Michel Jackson", 10.1, 1982, 'MJ', 1 ]

##Podemos concatenar las listas
Lista1 = Lista + [ "pop", 10 ]
print('Concatenacion de listas: ', Lista1)

#Tambien podemos concatenar dos listas a través de la funcion .extend()
Lista.extend( [ 'pop', 'class', 11 ] )
print('Uso de la funcion .extend() para añadir nuevos elementos a la lista: ', Lista)

#Se nos permite anexar o anidar una lista a la lista existente, con la funcion .append() 
Lista1.append( [ 'pop', 'class'] )
print('Usamos la funcion .append() para anidar una lista: ', Lista1)

#Como las listas son mutables podemos cambiar los elementos de una lista

Lista1[0] = 'Grogu'
print('Cambiamos el valor del indice 0', Lista1) 

#Podemos eliminar elementos de una lista con la funcion del()

del(Lista1[0])

print('Eliminamos la posición 0 de la lista1: ', Lista1)


#Podemos convertir una cadena a una lista usando la función .split()
listaConvert = "Hard Rock".split()
print('usamos la funcion .split(): ', listaConvert)

#Podemos usar la funcion de división para separar cadenas en un carácter específico conocido, como delimitador

delimitador = "A,B,C,D".split(",")
print(delimitador)

#Aliasing Lista = Lista, cualquier alteracion hecha en una se vera reflejada en la otra
#para clonar una lista es <nombreLista>[:] 

#Para obtner más información de una lista o tupla o otra cosa lo podemos hacer mediante la funcion help() 

