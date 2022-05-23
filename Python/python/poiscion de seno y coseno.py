# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return np.sin(x)


x = np.linspace(0, 10, 100)

plt.plot((x), h(x))

plt.grid()
plt.xlabel('Tiempo')
plt.ylabel('Posicion')
plt.title('Posición de Seno')

plt.plot(x, h(x), "r--", label="seno")


g = lambda X: np.cos(x)
plt.plot(x, g(x), label="Coseno de X")

#establecer el Rango en X y en Y (X,X,Y,Y)
v = (0, 10, -2, 2)
plt.axis(v)
plt.legend(loc=3)

