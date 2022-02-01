Tuple1 = ('disco', 10,2.2,3)
print('Impresion de la tupla 1', Tuple1)

#Imprime desde la posicion 0 dos pisicones 
print('Imprime dos posiciones a partir de la 0', Tuple1[0:2])

Tuple2 = Tuple1 + ('Hard rock', 100)

print ('fusion de dos tuplas', Tuple2)

#Con len se puede concer la longuitud de una tupla
print('La longitud de la tupla es: ', len(Tuple2))

#Las tuplas son inmutables,lo que significa que no podemos cambiarlas

#Para ordenar una tupla usamos la función sorted
Ratings = (10,3,12,5,2,1,6,8,9)
print("Tuple original", Ratings)
# De cierta forma, sorted ordena y regresa una nueva tuple
RatingsSorted = sorted(Ratings)
print("Tuple aplication of sorted", RatingsSorted)

#Existen tuplas anidadas
NewTuple = ( 1, 2, ( 'pop, rock' ), ( 3, 4 ), ( 'disco', ( 1, 2 ) ) )
           # 0  1         2             3               4
print(NewTuple[4])
print(NewTuple[4][1])