# The Basics & Array creation
# Una matriz Numpy (NP) es similar a una lista

import numpy as np

a = np.array([0, 1, 2, 3, 4])
print(a)

print(type(a))

# El tamaño de la matriz
print(a.size)

# Las dimenciones de la matriz
print(a.ndim)


c = np.array([20, 1, 2, 3, 4])
print(c)
# Cambia la el elemento que esta en la posición por uno nuevo
c[0] = 100
c[4] = 0
print(c)

# podemos cortar los elementos de un array en numpy y asíganarlos a otra
d = c[1:4]
print(c)
print(d)

# Podemos asiganar valores a las corrspondientes posiciones
c[3:5] = 200, 400

print(c)
