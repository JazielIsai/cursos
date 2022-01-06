#Cambia de estado un led si esta prendido recibe la señal y se apaga y vicerversa
from gpiozero import LED,Button#importamos librerias y clases
from time import sleep#importamos librerias y clases
led= LED(17)#Ceamos el objeto y lo conectamos al pin
button= Button(2)#Ceamos el objeto y lo conectamos al pin
while True:
    button.wait_for_press()#Si esta prendido
    led.toggle()#cambia de estado
    sleep(5)#Dura 5 segundos su estado
