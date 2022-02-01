from gpiozero import LED,Button#importamos librerias y clases
led= LED(17)#Ceamos el objeto y lo conectamos al pin
button= Button(2)#Ceamos el objeto y lo conectamos al pin
while True:
    if button.is_pressed:#Si el boton es presionado
        led.on#el boton enciende
        print("se presiono el botón y encendio el led")
    else:
        led.off()#Si suelta el boton se apaga
        print("no se ha presionado el botón, ni encendido el led")