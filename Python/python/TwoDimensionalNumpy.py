
# Multiplicación de matricez
import numpy as np

X = np.array([[1, 2], [2, 1]])
Y = np.array([[2, 3], [3, 2]])
z = X * Y
print(z)


X = np.array([[0, 1, 1], [1, 0, 1]])
Y = np.array([[1, 1], [1, 1], [1, -1]])
C = np.dot(X, Y)
print(C)

X = np.array([[1, 0], [0, 1]])
Y = np.array([[0, 1], [1, 0]])
Z = X + Y
print(Z)


X = np.array([[1, 0, 1], [2, 2, 2]])
out = X[0, 1:3]
print("out es:")
print(out)
