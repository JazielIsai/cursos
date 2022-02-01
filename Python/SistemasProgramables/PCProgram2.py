from gpiozero import LED#importar libreria para puerto de entrada y salida, importamos clase para los LED
from time import sleep#importar libreria time, importamos clase sleep
led= LED(17)#creamos objeto y especificamos a que pin esta conectado
while True:
    led.on()#Encendemos led
    sleep(0.5)#.5 segundos prendido
    led.off()#se apague el led
    sleep(1)#se apague 1 s y vuelve a iniciar el ciclo
