# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:05:07 2022

@author: jhazy
"""

import numpy as np
import matplotlib.pyplot as plt

#Definir una lista de paises tipo string

paises = [ 'Estados unidos', 'España', 'Mexico', 'Rusia', 'Japon' ]
valores = [ 25,33,34,40,27 ]
#Se declara el metodo/funcion AX para manejo de PLOTs en Barras
fig, ax=plt.subplots()
#colocar una etiqueta en x y en y, haciendo uso de ax
ax.set_ylabel('Valores')
ax.set_title('Cantidad de valores por pais')
plt.barh(paises, valores, alpha =0.8, color='blue')
plt.savefig('Grafica_Barras.png')
plt.show()