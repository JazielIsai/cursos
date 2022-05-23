lista = [5,4,6,8,4,2,1,0,9,3,2,5]

def SortList():
    temp = 0
    for i in range(1, len(lista)):
        for j in range(0, len(lista) - i):
            if(lista[j] < lista[j + 1]):
                temp = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = temp
    
    print("\n Lista Ordenada de mayor a menor es: \n", lista )

print(lista, '\n')
SortList()