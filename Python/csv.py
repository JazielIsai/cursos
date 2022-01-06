from matplotlib import pyplot as plt#libreria para graficar
with open ('/home/pi/Documents/datos.csv','r') as archivo:#mandamos a abrir los archivos
    print('Archivo: ')#imprimimos
    print(archivo)#imprimimos el archivo
    input()#esperamos
    print ('read(), lectura del archivo por renglones: <str>')#
    lineas=archivo.read()#leeos el achivo
    print(lineas)#imprimimos todas las lineas
    print(lineas[0],lineas[1],lineas[2],lineas[3])#imprimimos los elementos
    print(type(lineas))#tipo de datos
    input()
    print ('read(), lectura del archivo por renglones: <str>')
    archivo.seek(0)#regresar al primer elemento del archivo
    lineas2= archivo.readline()#leemos el archivo
    print(lineas2)
    print(lineas2[0],lineas2[1])
    print(type(lineas2))
    input()
    print ('read(), lectura del archivo por renglones: <list>')
    print('lista cada elemento es un string,cada elemento es un renglon')
    archivo.seek(0)
    lineas3= archivo.readline()
    print(lineas3)
    print(lineas3[0],lineas3[1])
    print(type(lineas3))
    input()
    print ('split(), lista separada por coma: <list>')
    print('lista cada elemento es un string')
    archivo.seek(0)
    lineas4= archivo.read().split(',')
    print(lineas4)
    print(lineas4[0],lineas4[1])
    print(type(lineas4))
    input()
    print ('splitlines(), lista seprada por lineas: <list>')
    print('lista cada elemento es un string')
    archivo.seek(0)
    lineas5= archivo.readline()
    print(lineas5)
    print(lineas5[0],lineas5[1])
    print(type(lineas))
    input()
    print('split(),cada renglon es una lista, cada elemento un string: <list>')
    for l in lineas5:
        linea= l.split(',')
        print(linea)
    print(linea)
    print(linea[0],lineas[1])
    print(type(lineas))
    input()
    print('split(),cada renglon es una lista, cada elemento un string: <list>')
    print('cada elemento un entero')
    archivo.seek(0)
    lineas6= archivo.read().splitlines()
    datos=[]
    for l in lineas6:
        linea2= l.split(',')
        datos.append([int(linea2[0]),int(linea2[1])])
    print(datos)
    print(datos[0],datos[1])
    print(type(datos))
    input()