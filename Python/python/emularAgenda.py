def Menu():
   
    print('MENÚ \n')
    print('CAPTURAR - Capturar Lista \n')
    print('MOSTRAR  - Mostrar lista \n')
    print('AGREGAR  - Agregar dígito \n')
    print('ELIMINAR - Eliminar dígito \n')
    print('BUSCAR   - Buscar dígito \n')
    print('ORDENAR   - Ordenar dígitos \n')
    print('SALIR    - Salir \n')

    opc =   input('Escribe una opción : ')
    opc = opc.upper()

    if ( opc ==  'CAPTURAR' ):
        Capture()
    elif ( opc ==  'MOSTRAR' ):
        Show()
    elif ( opc ==  'AGREGAR' ):
        Add()
    elif ( opc ==  'ELIMINAR' ):
        Delete()
    elif ( opc == 'BUSCAR' ):
        Search()
    elif ( opc == 'ORDENAR' ):
        SortList()
    else:
        exit()

def Capture():

    global lista

    lista= []

    stop =int(input(" Cuantos digitos tendra la lista?: \n"))

    #Comenzar a llenar los datos dede 0 hasta varn

    for i in range (0,stop):

        print("Ingresa el digito: ",i)

        #Se comienza a leer y guardar el digito

        digito = input()

        #insertar a la lista, trabajar con indice y el digito ingresado

        lista.insert(i,digito)

    Menu()



def Add():

    digito = int(input("\n Ingresa el digito que desea agregar: "))

    #validar q me de un numero entero

    indice = int(input("\n Ingrese el índice donde desea agregarlo: "))


    #Validar q el indice este dentro del rango de la lista

    if(indice > len(lista) or indice < 0):

        print("El indice debe estar entre 0 y ", len(lista))

    else:

        lista.insert(indice, digito)

        print("\n Digito agregado")

    Menu()



def Show():

    print(lista)

    Menu()



def Delete():

    indice = int(input("\n Ingrese el índice que desea eliminar: "))

    #Validar q el indice este dentro del rango de la lista

    if(indice > len(lista) or indice < 0):
        print("El indice debe estar entre 0 y ", len(lista)-1)

    else:

        del(lista[indice])

        print("\n Se ha eliminado el digito")

    Menu()

def Search():

    buscar = int(input("\n Ingresa el indice del dijito que buscas: "))
    
    print( [lista[buscar]] )
    
    Menu()


def SortList():
    temp = 0
    for i in range(1, len(lista)):
        for j in range(0, len(lista) - i):
            if(lista[j + 1] < lista[j]):
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    
    print("\n Lista Ordenada es: \n", lista )
    
    Menu()


#corerr el codigo empiza desde el menu

Menu()