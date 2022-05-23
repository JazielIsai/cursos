import random

def DetectarDuplicado (lista):
    if ( set(lista) ):
        return True
    else:
        return False
    
def ElementosAleatorios():
    numeros = []
    for i in range(0, 23):
        numeros.append( random.randrange(0, 100) )
    print (numeros)
    return numeros


print(DetectarDuplicado(ElementosAleatorios()))     