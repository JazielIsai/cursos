from gpiozero import LightSensor 
from time import sleep, strftime, time
import matplotlib.pyplot as plt

ldr = LightSensor(4) 

Hora = []
Sensor = []
Fecha = []

n = int(input("Ingrese la cantidad de muestras \n"))
print(n)
print()

for x in range(n):
    print("Obtener intensidad luminosa, fecha y hora")
    input()
    x= ldr.value
    print(x)
    print("{0:.4f}".format(x))
    xr0= round(x) 
    xr= round(x,3)
    print()
    Sensor.append(xr)
    
    h= strftime("%H:%M:%S")
    print(h)
    Hora.append(h)
    
    f = strftime("%d-%m-%y")
    print(f)
    Fecha.append(f)
    print()
    
input()

print(Sensor)
print(Hora)
print(Fecha)

fig = plt.figure()
ax = fig.add_subplot(111)

xx = range(1,len(Sensor)+1)

ax.bar(xx,Sensor, width = 0.5, color = (0,0,1), align= "center")
ax.set_xticks(xx)
ax.set_yticklabels(Hora)
ax.set_ylabel("Intensidad")

plt.show()