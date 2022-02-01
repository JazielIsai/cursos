from gpiozero import LED#importar libreria para puerto de entrada y salida, importamos clase para los LED
from time import sleep#importar libreria time, importamos clase sleep
led= LED(17)#creamos objeto y especificamos a que pin esta conectado
button= Button(2)#Creamos el objeto y pasamos el argumento al pin 2

while True:
    print()#dejamos espacios en blanco
    print()#
    print()#
    print('no se ha presionado el boton')#decimos que no se ha presionado el boton
    print()#
    print()#
    a= button.wait_for_press()#la funcion detecta cuando al pin llega una señal
    print(a, ', se ha presionado el boton')#si llega la señal imprime la leyenda y enciende el led
    print()
    b=led.on()
    print(b, ', se ha encendido el led 5 seg')#
    print()#
    sleep(5)#enciende por 5 seg
    print ('hola, despues de 5 seg.')#manda mensaje 
    led.off()
    button.wait_for_release()
    print()#
    print('Se ha soltado el boton y apagado el led')#manda mensaje de que se solto el boton y se apaga el led 