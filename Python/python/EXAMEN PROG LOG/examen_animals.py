# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 08:22:32 2022

@author: jhazy
"""

import pandas as pd

animals = pd.read_csv("examen.csv", index_col=0, encoding='latin-1' )
#print(animals)


def machos_hembras(sex_animals):
    try:
        result = animals[ (animals['sexo'] == sex_animals) ]
        print(sex_animals, ': ', len(result))
        return result
    except Exception as err:
        print(err)


#print('Los machos: \n', machos_hembras('M'))
#print('Las hembras: \n', machos_hembras('F'))


def especies_registrados(year_animals):
    try:
        result = animals[ ( animals['año'] == year_animals ) ]
        result = set(result['idespecie'])
        print(year_animals, ': ', len(result))
        
        return result 
    except Exception as err:
        print(err)
        
        
# print( especies_registrados(2001) )

def registrados_sitio(sitio_animals):
    try:
        result = animals[ (animals['idsitio'] == sitio_animals) ]
        result = set(result['idespecie'])
        print('Sitio es: ', sitio_animals, ' y existen: ', len(result))
        return(result)
    except Exception as err:
        print(err)
        

# print(registrados_sitio(4))


#Esta es la 5
def especies_x_idsitio():
    try:
        result = animals[ ( animals('idsitio').unique().tolist() )   ]
        return result
    except Exception as err:
        print(err)

# print(especies_x_idsitio())


def machos_registrados(sex_animals, year_animals, peso_animals):
    try:
        result = animals[ (animals['sexo'] == sex_animals ) & (animals['año'] ==  year_animals) & (animals['peso'] > peso_animals ) ]
        print( 'Sex: ', sex_animals,  ' year: ', year_animals, ' peso: ', peso_animals, 'son en total: ', len(result));
        return result
    except Exception as err:
        print(err)    
        
#print(machos_registrados('M', 1999, 30))


def pregunta_siete(especie_animals, sex_animals, sitio_animals, peso_animals1, peso_animals2):
    try:
        result = animals[ ( animals['idespecie'] == especie_animals ) & (animals['sexo'] == sex_animals) & (animals['idsitio'] == sitio_animals) & (animals['peso'] >= peso_animals1) & (animals['peso'] <= peso_animals2 )  ]
        print( 'son en total: ', len(result));
        return result
    except Exception as err:
        print(err)    


#print( pregunta_siete('PB', 'F', 8, 25, 30) )


def pregunta_registradas(mes, dia):
    try:
        result = animals[ ( animals['año'] == mes) & (animals['idsitio'] == dia) ]
        result = set(result['idespecie'])
        print(': ', len(result))
        
        return result 
    except Exception as err:
        print(err)
        
#print( pregunta_registradas(1988, 22) )




