# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 08:58:52 2022

@author: mario
"""
import pandas as pd
import matplotlib.pyplot as plt

#Leer el archivo .csv

datos=pd.read_csv(r"C:\/Users\/mario\/Documents\/8vo\/PLF\/U3\/titanic\/titanic.csv")
#para ver el encabezado y primeras 5 lineas
#print(datos.head())
#Para ver el tipo de datos de cada campo
#print(datos.info())
#print(datos.describe())
#Para saber cual es la edad media
#print(datos.Age.median())
#cuantos hombres y mujeres hay en el archivo
#print(datos.Sex.value_counts())
#ver cuantos gombres y mujeres sobrevivientes hay
print("Datos de los sobrevivientes")
sobrevivientes= datos[datos.Survived==1].Sex.value_counts()
print(sobrevivientes)
print('Muertitos')
muertitos= datos[datos.Survived==0].Sex.value_counts()
print(muertitos)
#dataframe,comparar dos variables(muertos,sobrevivientes)
df1=pd.DataFrame([sobrevivientes,muertitos],index=['Survived','Dead'])
df1.plot.bar()
#para ver el grafico de una manera mas comprensible,utilizar kind
df1.plot(kind='bar',stacked=True)
df1.show()