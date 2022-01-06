import matplotlib.pyplot as plt

fig= plt.figure()
ax1= fig.add_subplot(121)
ax2= fig.add_subplot(122)

alumnos1 = ["Hugo", "Paco", "Luis", "Diana", "Jorge"]
datos1= [2,4,6,8,10]
xx1= range(1,len(datos1)+1)

alumnos2 = ["Pedro", "David", "Juan", "Ximena", "Sofia"]
datos2= [1,3,5,7,9]
xx1= range(1,len(datos2)+1)

ax1.bar(xx1, datos1, width=0.5, color=(0,0,1), align ="center")
ax1.set_xticks(xx1)
ax1.set_xtickslabels(alumnos1)
ax1.set_ylabel("calificaciones")

ax2.bar(xx2, datos2, width=0.5, color=(0,0,1), align ="center")
ax2.set_xticks(xx2)
ax2.set_xtickslabels(alumnos2)
ax2.set_ylabel("calificaciones")

plt.show()