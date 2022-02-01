#led parpadea
from gpiozero import LED,Button#importamos librerias y clases
from time import sleep#importamos librerias y clases
led= LED(17)#Ceamos el objeto y lo conectamos al pin
button= Button(2)#Ceamos el objeto y lo conectamos al pin
button.wait_for_press()#cuando se oprime el boton ejecuta la función de parpadear
led.blink()#parpadea