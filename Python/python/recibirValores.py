print('Conjunción AND \n')
var1 = int(input('Escribe un número mayor a 2 y menor a 5 porfis: '))

if (var1 > 2) and (var1 < 5):
    print('El numero', var1, "Cumple con la condición \n")
else:
    print('El numero', var1, "No cumple con la condición \n")


##OR
print('Conjunción OR \n')
palabra = input('Para cumplir la condición escribe SI o YES: ')

if palabra == 'YES' or palabra=='SI':
    print('La condición se ha cumplido \n')
else:
    print('La condición no se ha cumplido \n')