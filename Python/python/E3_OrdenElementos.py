def ordenada(lista):
    if( sorted(lista, reverse=False) ):
        return 'Lista ordenada y de forma ascendente'
    else:
        return 'Lista no ordenada'


listaAsendente = [ 1,2,3,4,5,6,7,8,9,10,11 ]
listaNoOrdenada = [ 11,10,9,12,7,6,4,4,3,2,1 ]

print (ordenada(listaAsendente))
