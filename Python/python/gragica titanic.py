# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 08:42:12 2022

@author: jhazy
"""

import pandas as pnd
import matplotlib.pyplot as plt

df = pnd.read_csv('titanic.csv')
# print(df);


df2 = pnd.read_csv('titanic.csv')
#print(df2);

pclass = df2['PClass']
numPeople = len(df2)
survived = df2['Survived']
sex = df2['Sex']
age = df2['Age']

datosPeople = []

# print(numPeople)


#cuantos hombres o mujeres mayores de 18 años murieron en el titanic
def age_function( agePeople, sexPeople ):
    suma = 0
    for i in range(0, numPeople):
        if age[i] >= agePeople and sex[i] == sexPeople and age[i] != '':
            #print('edad: ', age[i], '  ....   sexo: ', sex[i])
            suma += 1;
    return suma;


print('Hombres mayores a 18: ', age_function(18, 'male') )

print('Mujeres mayores a 18: ', age_function(18, 'female') )


#Personas que sobrevieron o murieron definiendo una clase

def plcass_function ( pclass_people, survived_people ):
    suma = 0
    for i in range(0, numPeople ):
        if pclass[i] == pclass_people and survived[i] == survived_people:
            suma += 1
    return suma

print('3 clase murieron: ', plcass_function('3rd', 0) )
print('2 clase sobrevivieron: ', plcass_function('2nd', 1) )




def plcass_sex_function ( pclass_people, survived_people, sexPeople ):
    suma = 0
    for i in range(0, numPeople ):
        if pclass[i] == pclass_people and survived[i] == survived_people and sex[i] == sexPeople:
            suma += 1
    return suma


# print( '1 clase mujeres que sobrevivieron', plcass_sex_function('') )


# CUANTAS MUJERES DE ENTRE 20 Y 40 AÑOS SOBREVIVIERON EN EL TITANIC.
    
def male_suvervir ():
    result  =   df[ (df['Sex']=='female') & (df['Age']>=20) & (df['Age']<=40) & (df['Survived'] ==  1)]
    print('MUJERES DE ENTRE 20 Y 40 AÑOS SOBREVIVIERON : ', len(result) )
    return result;


print(male_suvervir())