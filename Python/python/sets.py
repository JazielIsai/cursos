#Los sets son un tipo de colección de datos

#Estas listas o colecciones estan desordenadas
# es decir, no registran una posición

set1 = {"pop", "rock", "soul", "hard rock", "rock", "disco"}
set1.remove("pop")
set1.add("NYSNC")
#cuando se crean elementos duplicados, no estarán presentes,
#de cierta forma se eliminarán

#se puede convertir una lista a un conjunto mediante el uso del
#conjunto de funciones, set() esto se llama tipo casting.
set(list)

"AC/DC" in set1 #para verificar si existe el elemento en set1


#para conocer que elementos son iguales dentro de dos sets se usa el & en medio de los dos conjutnos
