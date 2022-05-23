#Dicionarios en python

#Un diccionario tiene claves y valores
# La clave es análoga al indice
# Dictionaries are denoted with curly Brackets {}
#The key have to be inmutable and unique
#The value can be can inmutable, mutable, and duplicates

dictionary = {
    "thriller": 1992,
    "Back in black": 1980,
    "The Dark side of the moon": 1973,
    "The bodyguard": 1992
}

#Para acceder a un valor, accedemos de la siguiente manera 
#   dictionary["thiller"] y el valor que devolvería será: 1992

#podemos eliminar algun elemento y clave con la palabra reservada del(DICT['key'])

#podemos agregar valores al diccionario usando el nombre del diccionario, ejemplo DICT['key'] = valor

#Además podemos verificar si existe un elemento con la palabra in
#ejemplo: 'key' in 'name_dictionary'

#para acceder a las keys y a los values es 
# name_dictionary.key() o name_dictionary.values()