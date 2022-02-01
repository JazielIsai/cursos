from gpiozero import LightSensor#importar la libreria para puerto general o puertos genericos
import matplotlib.pyplot as plt#libreria para hacer graficas
ldr=LightSensor(4)#nuestra resistencia, pin 4 
Iluminacion= ["lampara apagada","lampara encendida","luz celular"]#lista con cadenas que son los estados de la lecturra del sensor
Sensor=[]#Lista vacia para guardar los valores que nos regrese la función
print("Apague la luz")#mandamos mensaje para que apaguen la luz 
input()#espera que apaguemos la luz y damos enter
print(ldr.value)#detecta la intencidad luminosa y el valor lo asigna a ldr
x=ldr.value#se guarda en la variable x
print(x)#imprimimos x
Sensor.append(x)#anexamos a la lista vacia
input()#enter para la siguiente condición siguiente
print("Encienda la luz")
input()
print(ldr.value)
x=ldr.value
print(x)
Sensor.append(x)
input()
print("Encienda la luz del celular")
input()
print(ldr.value)
x=ldr.value
print(x)
Sensor.append(x)
input()
print(Iluminacion)#mandamos las listas
print(Sensor)#imprimimos las listas de los valores 
#librerias
fig=plt.figure()#Figura a graficar
ax=fig.addsubplot(111)#subdividida la pantalla 1 columna 1 renglon
xx=range(1, len(Sensor)+1)#rango de valor inicia en 1 hasta el rango del sensor mas 1
ax.bar(xx,Sensor,width=0.5,color=(0,0,1),aling='center')#graficar eje x variable sensor,ancho,color y cada barra en el centro
ax.set_xticks(xx)#variables en el eje x
ax.set_xticklabels(Iluminacion)#valor a graficar 
ax.set_ylabeñ('Sensor')#valor eje y sensor
plt.show()
       