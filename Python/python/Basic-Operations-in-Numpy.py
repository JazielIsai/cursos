
# Basic Operations in Numpy
# Numpy hace que sea más facil algunas operaciones
import numpy as np

# u = [1, 0]
# v = [0, 1]
# z = []
# for n, m in zip(u, v):
#    z.append(n + m)
# print(z)

u = np.array([1, 0])
v = np.array([0, 1])
z = u - v
print("Resta", z)

# Multiplicación vectorial con un escalar solo
# requiere una linea de código usando numpy.
y = np.array([1, 2])
z = 2 * y
print("Multiplicación vectorial", z)

# Product of two numpy arrays
a = np.array([1, 2])
b = np.array([3, 4])
c = a * b
print("Product of two numpy array", c)

# Dot Product
d = np.array([1, 2])
e = np.array([3, 1])
result = np.dot(d, e)
print("Dot Product", result)

# Universal Functions
a = np.array([1, -1, 1, -1])
mean_a = a.mean()
print(mean_a)

# Podemos encontrar el valor maximo
b = np.array([1, -2, 3, 4, 5])
max_b = b.max()
print(max_b)

# Functions Universal
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)
print(y)

# De -2 a 2 corre 9 posiciones
f = np.linspace(-2, 2, num=9)
print(f)
