#Apagar y encender el led
from gpiozero import LED,Button#importamos librerias y clases
from signal import pause
led= LED(17)#Ceamos el objeto y lo conectamos al pin
button= Button(2)#Ceamos el objeto y lo conectamos al pin
button.when_pressed= led.on#Cuando el boton es presionado el led enciende
button.when_released= led.off#Cuando el boton no es presionado el led se apaga
pause()
