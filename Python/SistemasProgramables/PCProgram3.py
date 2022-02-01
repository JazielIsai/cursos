#Un push button
from gpiozero import Button#Importamos libreria para manejar puerto de entrada y salida, importamos la clase Button
button= Button(2)#Creamos el objeto y pasamos el argumento al pin 2
while True:
    print()#dejamos espacios en blanco
    print()#
    print()#
    print('no se ha presionado el boton')#decimos que no se ha presionado el boton
    a= button.wait_for_press()#la funcion detecta cuando al pin llega una señal
    print()
    print(a, ', se ha presionado el boton')#si llega la señal imprime la leyenda
    print()
    button.wait_for_release()#detecta si no llega una señal al pin
    print('se ha soltado el boton')#manda mensaje de que se solto el boton
