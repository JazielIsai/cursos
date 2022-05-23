
salir = True

while salir:
    print("Menu \n 1) Nuevo \n 2) Mostrar \n 3) Eliminar \n 4) Agregar Lista \n 5) Salir")
    opcion = int(input('Elige una opción:  '))
    i = 0
    if opcion == 1:
        print('Nuevo registro: \n ')
        archivo = open('misdatos.csv', 'a')
        nombre = input('Ingresa el nombre: ')
        telefono = input('Ingresa el telefono: ')
        archivo.write(nombre)
        archivo.write(',')
        archivo.write(telefono)
        archivo.write(',')
        archivo.write('\n')
        archivo.close()
        
        print('Los datos se han guardado correctamente, el nombre fue: ', nombre, 'el telefono: ', telefono)

    elif (opcion == 2):
        
        print('Los registros: \n')
        archivo = open('misdatos.csv', 'r')
        mostrar = archivo.read()
        print(mostrar)
        archivo.close()
        
    elif (opcion == 3):

        print('Eliminar archivo: \n')
        archivo = open('misdatos.csv', 'a')
        archivo.truncate(0)
        print('LOS DATOS HAN SIDO ELIMINADOS')    

    elif (opcion == 4):
        print('Agregar una lista de 5 numeros: \n')
        lista = []
        while (i != 5):
            i += 1
            lista.append( int(input('Ingresar Numero: ')) )
        archivo = open('misdatos.csv', 'a')
        archivo.write(str(lista))
        archivo.write(',')
        archivo.write('\n')
        archivo.close()
        
    elif (opcion == 5):
        print('salir')
        salir = False
    
    else:
        print ('Neceistas escoger alguna opcion para realizar alguna operación.')

