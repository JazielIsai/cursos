
import numpy as np
import matplotlib.pyplot as plt

partidos = []
resultados = ['G', 'P', 'E']
gano = 0
empato = 0
perdio = 0

score = 0

with open('partidosMilan.csv', 'r') as file:
    for line in file:
        partidos.append(line.split(sep=','))
        print(line.split(sep=','))

fig, ax = plt.subplots()
ax.set_ylabel('partidos')
ax.set_title('resultados')
for i in range(0, len(partidos)):
    if partidos[i][1] == 'G':
        gano += score + 1
        plt.barh(resultados[0], gano, alpha=0.8, color='blue')
    elif partidos[i][1] == 'E':
        empato += score + 1
        plt.barh(resultados[2], empato , alpha=0.8, color='blue')
    elif partidos[i][1] == 'P':
        perdio += score + 1
        plt.barh(resultados[1], perdio , alpha=0.8, color='blue')

print('Gano', gano, 'perdio', perdio, 'empato', empato)

plt.show()