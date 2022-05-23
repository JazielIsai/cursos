# -*- coding: utf-8 -*-
"""
Created on Tue May  3 09:20:39 2022

@author: jhazy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy


# pd.read_csv?

df = pd.DataFrame({'1stcolumn':[100,200], '2ndcolumn':[10,20]}) # esto crea un __DataFrame__ para el ejemplo!
print('With the old column names:\n') # El \n crea una nueva línea, para que sea más fácil de ver
print(df)

df.columns = ['FirstColumn','SecondColumn'] # renombra las columna!
print('\n\nWith the new column names:\n')
print(df)

# surveys = pd.read_csv("/Aemet2022-01-01.csv")
# my_plot = surveys.plot("Estación", "Temperatura máxima (ºC)", kind="scatter")
# plt.show() # no necesariamente en Jupyter Notebooks


sample_data = numpy.random.normal(0, 0.1, 1000)
plt.hist(sample_data)


fig, ax = plt.subplots()  # initiate an empty figure and axis matplotlib object
ax.hist(sample_data, 30)

fig, ax1 = plt.subplots() # preparar un gráfico con matplotlib
ax1.hist(sample_data, 30)

# Crear el gráfico de una distribución Beta
a = 15
b = 20
beta_draws = numpy.random.beta(a, b)
# editar las etiquetas
ax1.set_ylabel('density')
ax1.set_xlabel('value')

# añadir ejes adicionales a la figura
ax2 = fig.add_axes([0.125, 0.575, 0.3, 0.3])
# ax2 = fig.add_axes([left, bottom, right, top])
ax2.hist(beta_draws)


