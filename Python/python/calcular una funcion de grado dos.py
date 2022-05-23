# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 08:29:28 2022

@author: jhazy
"""

import numpy as np
import matplotlib.pyplot as plt

#variables independiente "arange" (valor inicial, incremento)
x = np.arange(0,10,0.1)
#se genera una variable "y" para cacular la función del COS de x

y = x * np.cos(x)
plt.plot(x, y)
plt.Xlabel("x")
plt.Ylabel("y")
plt.title("Grafica")