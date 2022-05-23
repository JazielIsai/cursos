


def promedios (cal1, cal2, cal3, cal4):

    if(cal1 >= 70) and (cal2 >= 70) and (cal3 >= 70) and (cal4 >= 70):
        TuplaSma = (cal1, cal2, cal3, cal4)
        for i in TuplaSma:
            promedio =+ i
            print ('cal1: ', i)
        print('Has pasado la Materia') 
        promedio = 'A'
    else:
        print ('Has reprobado la materia, necesita esmerarse')
        promedio = 'NA'
    
    return promedio
    
print( promedios(80,90, 100, 80) )