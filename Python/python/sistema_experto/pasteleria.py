
conlusion = ""
people = 0
precio = 0

print("Bienvenido a la pasteleria la cereza")
response = input("¿Desea un pastel? \n Si / No  ---> \t")
print("Su respuesta ha sido: " + response + " ")

if response == "Si":
    conlusion = conlusion + "Desea un pastel "
    
    people = int(input("¿Para cuantas personas es? ---> \t "))
    conlusion = conlusion + " para una cantidad de " + str(people) + " de personas "
    
    print("¿Desea un tamaño especial? o ¿En base a la cantidad de personas se define el tamaño del pastel? \n Como nota importante: Nosotros vendemos el pastel por tamaños y no por kilos")
    questionSize = input("---> \t ")
    if questionSize == "En base a la cantidad de personas":
        if int(people) <= 15:
            conlusion = conlusion + "Tamaño del pastel será: chico"
            precio = people * 25
        elif int(people) <= 50:
            conlusion = conlusion + "Tamaño del pastel será: mediano"
            precio = people * 25
        elif int(people) <= 100:
            conlusion = conlusion + "Tamaño del pastel será: grande"
            precio = people * 25
        elif int(people) <= 150:
            conlusion = conlusion + "Tamaño del pastel será: extra grande"
            precio = people * 25
        elif int(people) > 150:
            conlusion = conlusion + "Tamaño del pastel será: extra extra grande"
            precio = people * 25
    else:
        conlusion = conlusion + " con un tamaño de: " + questionSize
        
    print("El precio por el pastel será: " + str(precio))
        
    print("Los eventos son: Boda, Cumpleaños, Quince Años, Aniversarios, Fista infantil, Despedidas, Día de la madre, Día del padre, Casual ")
    event = input("¿Para que evento es el pastel?  ---> \t")
    conlusion = conlusion + " y el evento es: " + event
    
    if event == "boda":
        taste = input("¿De que sabor lo desea? ---> \t")
        if taste == "Recomiendeme uno" or taste == "Nose" or taste == "que sabor es comun para boda":
            print("Los sabores que se dan comunmente en bodas son: vainilla, marmoleado, moka y naranja")
            tasteOps = input("Entonces el sabor de su pastel será: ---> \t")
            conlusion = conlusion + ", el sabor del pastel será: " + tasteOps
        else :
            conlusion = conlusion + ", el sabor del pastel será: " + taste
        
        print("El pastel en pisos es un pastel escalonado donde lleva una base y sobre de ella otra pero más chica y así sucesivamente \n y en plancha es un pastel rectangulas o circular sin ninguna escala ") 
        cakeType = input("¿El pastel lo desea en pisos o en plancha? ---> \t")
        conlusion = conlusion + ", el pastel será en: " + cakeType
        
        decorationCake = input("Describe la decoración que desea que tenga el pastel: ---> \t")
        conlusion = conlusion + " y la decoración será: " + decorationCake
        
        print("================================")
        print("El fondant es una pasta parecida a la plastilina pero comestible, empleada como recubrimiento de ciertas preparaciones como bollos, pasteles, magdalenas, etc. En la mayoría de los casos el fondant es una decoración repostera")
        print("Chantully se trata de una crema espesa y dulce. ")
        print("Creama Pastelera es una crema dulce ")
        print("El betún es una crema a base de mantequilla y azúcar.")
        decorationOps = input("La decoración que menciono: ¿la desea en fondant, en crema, betun, chantilly? ---> \t")
        if decorationOps == "fondant" or decorationOps == "crema" or decorationOps == "betun" or decorationOps == "chantilly":
            conlusion = conlusion + " y la decoración será: " + decorationOps
        else:
            conlusion = conlusion + " y la decoración será: " + decorationOps
        
        
    elif event == "cumpleaños":
        taste = input("¿De que sabor lo desea? ---> \t")
        if taste == "Recomiendeme uno" or taste == "Nose" or taste == "que sabor es comun para un cumpleaños":
            print("Los sabores que se dan comunmente en los cumpleaños son: vainilla, chocolate, red velvet y marmoleado")
            tasteOps = input("Entonces el sabor de su pastel será: ---> \t")
            conlusion = conlusion + ", el sabor del pastel será: " + tasteOps
        else :
            conlusion = conlusion + ", el sabor del pastel será: " + taste
        
        print("El pastel en pisos es un pastel escalonado donde lleva una base y sobre de ella otra pero más chica y así sucesivamente \n y en plancha es un pastel rectangulas o circular sin ninguna escala ") 
        cakeType = input("¿El pastel lo desea en pisos o en plancha? ---> \t")
        conlusion = conlusion + ", el pastel será en: " + cakeType
        
        decorationCake = input("Describe la decoración que desea que tenga el pastel: ---> \t")
        conlusion = conlusion + " y la decoración será: " + decorationCake
        
        print("================================")
        print("El fondant es una pasta parecida a la plastilina pero comestible, empleada como recubrimiento de ciertas preparaciones como bollos, pasteles, magdalenas, etc. En la mayoría de los casos el fondant es una decoración repostera")
        print("Chantully se trata de una crema espesa y dulce. ")
        print("Creama Pastelera es una crema dulce ")
        print("El betún es una crema a base de mantequilla y azúcar.")
        decorationOps = input("La decoración que menciono: ¿la desea en fondant, en crema, betun, chantilly? ---> \t")
        if decorationOps == "fondant" or decorationOps == "crema" or decorationOps == "betun" or decorationOps == "chantilly":
            conlusion = conlusion + " y la decoración será: " + decorationOps
        else:
            conlusion = conlusion + " y la decoración será: " + decorationOps
        
    
    elif event == "aniversario":
        taste = input("¿De que sabor lo desea? ---> \t")
        if taste == "Recomiendeme uno" or taste == "Nose" or taste == "que sabor es comun para un aniversario":
            print("Los sabores que se dan comunmente en los aniversarios son: vainilla, marmoleado, moka y naranja")
            tasteOps = input("Entonces el sabor de su pastel será: ---> \t")
            conlusion = conlusion + ", el sabor del pastel será: " + tasteOps
        else :
            conlusion = conlusion + ", el sabor del pastel será: " + taste
        
        print("El pastel en pisos es un pastel escalonado donde lleva una base y sobre de ella otra pero más chica y así sucesivamente \n y en plancha es un pastel rectangulas o circular sin ninguna escala ") 
        cakeType = input("¿El pastel lo desea en pisos o en plancha? ---> \t")
        conlusion = conlusion + ", el pastel será en: " + cakeType
        
        decorationCake = input("Describe la decoración que desea que tenga el pastel: ---> \t")
        conlusion = conlusion + " y la decoración será: " + decorationCake
        
        print("================================")
        print("El fondant es una pasta parecida a la plastilina pero comestible, empleada como recubrimiento de ciertas preparaciones como bollos, pasteles, magdalenas, etc. En la mayoría de los casos el fondant es una decoración repostera")
        print("Chantully se trata de una crema espesa y dulce. ")
        print("Creama Pastelera es una crema dulce ")
        print("El betún es una crema a base de mantequilla y azúcar.")
        decorationOps = input("La decoración que menciono: ¿la desea en fondant, en crema, betun, chantilly? ---> \t")
        if decorationOps == "fondant" or decorationOps == "crema" or decorationOps == "betun" or decorationOps == "chantilly":
            conlusion = conlusion + " y la decoración será: " + decorationOps
        else:
            conlusion = conlusion + " y la decoración será: " + decorationOps
        
        
    elif event == "fiesta infantil" or event == "fista de niños":
        taste = input("¿De que sabor lo desea? ---> \t")
        if taste == "Recomiendeme uno" or taste == "Nose" or taste == "que sabor es comun para una fiesta de niños":
            print("Los sabores que se dan comunmente en las fiestas para niños son: Vainilla, chocolate, marmoleado y piña")
            tasteOps = input("Entonces el sabor de su pastel será: ---> \t")
            conlusion = conlusion + ", el sabor del pastel será: " + tasteOps
        else :
            conlusion = conlusion + ", el sabor del pastel será: " + taste
        
        print("El pastel en pisos es un pastel escalonado donde lleva una base y sobre de ella otra pero más chica y así sucesivamente \n y en plancha es un pastel rectangulas o circular sin ninguna escala ") 
        cakeType = input("¿El pastel lo desea en pisos o en plancha? ---> \t")
        conlusion = conlusion + ", el pastel será en: " + cakeType
        
        decorationCake = input("Describe la decoración que desea que tenga el pastel: ---> \t")
        conlusion = conlusion + " y la decoración será: " + decorationCake
        
        print("================================")
        print("El fondant es una pasta parecida a la plastilina pero comestible, empleada como recubrimiento de ciertas preparaciones como bollos, pasteles, magdalenas, etc. En la mayoría de los casos el fondant es una decoración repostera")
        print("Chantully se trata de una crema espesa y dulce. ")
        print("Creama Pastelera es una crema dulce ")
        print("El betún es una crema a base de mantequilla y azúcar.")
        decorationOps = input("La decoración que menciono: ¿la desea en fondant, en crema, betun, chantilly? ---> \t")
        if decorationOps == "fondant" or decorationOps == "crema" or decorationOps == "betun" or decorationOps == "chantilly":
            conlusion = conlusion + " y la decoración será: " + decorationOps
        else:
            conlusion = conlusion + " y la decoración será: " + decorationOps
        
    
    elif event == "quince años":
        taste = input("¿De que sabor lo desea? ---> \t")
        if taste == "Recomiendeme uno" or taste == "Nose" or taste == "que sabor es comun para una quince años":
            print("Los sabores que se dan comunmente en las fiestas para quince años son: vainilla, marmoleado, moka y naranja")
            tasteOps = input("Entonces el sabor de su pastel será: ---> \t")
            conlusion = conlusion + ", el sabor del pastel será: " + tasteOps
        else :
            conlusion = conlusion + ", el sabor del pastel será: " + taste
        
        print("El pastel en pisos es un pastel escalonado donde lleva una base y sobre de ella otra pero más chica y así sucesivamente \n y en plancha es un pastel rectangulas o circular sin ninguna escala ") 
        cakeType = input("¿El pastel lo desea en pisos o en plancha? ---> \t")
        conlusion = conlusion + ", el pastel será en: " + cakeType
        
        decorationCake = input("Describe la decoración que desea que tenga el pastel: ---> \t")
        conlusion = conlusion + " y la decoración será: " + decorationCake
        
        print("================================")
        print("El fondant es una pasta parecida a la plastilina pero comestible, empleada como recubrimiento de ciertas preparaciones como bollos, pasteles, magdalenas, etc. En la mayoría de los casos el fondant es una decoración repostera")
        print("Chantully se trata de una crema espesa y dulce. ")
        print("Creama Pastelera es una crema dulce ")
        print("El betún es una crema a base de mantequilla y azúcar.")
        decorationOps = input("La decoración que menciono: ¿la desea en fondant, en crema, betun, chantilly? ---> \t")
        if decorationOps == "fondant" or decorationOps == "crema" or decorationOps == "betun" or decorationOps == "chantilly":
            conlusion = conlusion + " y la decoración será: " + decorationOps
        else:
            conlusion = conlusion + " y la decoración será: " + decorationOps
        
        
    elif event == "despedidas":
        taste = input("¿De que sabor lo desea? ---> \t")
        if taste == "Recomiendeme uno" or taste == "Nose" or taste == "que sabor es comun para una despedidas":
            print("Los sabores que se dan comunmente en las despedidas: vainilla, chocolate, red velvet, naranja, marmoleado, cafe, moka ")
            tasteOps = input("Entonces el sabor de su pastel será: ---> \t")
            conlusion = conlusion + ", el sabor del pastel será: " + tasteOps
        else :
            conlusion = conlusion + ", el sabor del pastel será: " + taste
        
        print("El pastel en pisos es un pastel escalonado donde lleva una base y sobre de ella otra pero más chica y así sucesivamente \n y en plancha es un pastel rectangulas o circular sin ninguna escala ") 
        cakeType = input("¿El pastel lo desea en pisos o en plancha? ---> \t")
        conlusion = conlusion + ", el pastel será en: " + cakeType
        
        decorationCake = input("Describe la decoración que desea que tenga el pastel: ---> \t")
        conlusion = conlusion + " y la decoración será: " + decorationCake
        
        print("================================")
        print("El fondant es una pasta parecida a la plastilina pero comestible, empleada como recubrimiento de ciertas preparaciones como bollos, pasteles, magdalenas, etc. En la mayoría de los casos el fondant es una decoración repostera")
        print("Chantully se trata de una crema espesa y dulce. ")
        print("Creama Pastelera es una crema dulce ")
        print("El betún es una crema a base de mantequilla y azúcar.")
        decorationOps = input("La decoración que menciono: ¿la desea en fondant, en crema, betun, chantilly? ---> \t")
        if decorationOps == "fondant" or decorationOps == "crema" or decorationOps == "betun" or decorationOps == "chantilly":
            conlusion = conlusion + " y la decoración será: " + decorationOps
        else:
            conlusion = conlusion + " y la decoración será: " + decorationOps
        
    
    elif event == "día de las madres":
        taste = input("¿De que sabor lo desea? ---> \t")
        if taste == "Recomiendeme uno" or taste == "Nose" or taste == "que sabor es comun para el día de las madres":
            print("Los sabores que se dan comunmente para el día de las madres son: vainilla, naranja, marmoleado, cafe, moka, 3 leches  ")
            tasteOps = input("Entonces el sabor de su pastel será: ---> \t")
            conlusion = conlusion + ", el sabor del pastel será: " + tasteOps
        else :
            conlusion = conlusion + ", el sabor del pastel será: " + taste
        
        print("El pastel en pisos es un pastel escalonado donde lleva una base y sobre de ella otra pero más chica y así sucesivamente \n y en plancha es un pastel rectangulas o circular sin ninguna escala ") 
        cakeType = input("¿El pastel lo desea en pisos o en plancha? ---> \t")
        conlusion = conlusion + ", el pastel será en: " + cakeType
        
        decorationCake = input("Describe la decoración que desea que tenga el pastel: ---> \t")
        conlusion = conlusion + " y la decoración será: " + decorationCake
        
        print("================================")
        print("El fondant es una pasta parecida a la plastilina pero comestible, empleada como recubrimiento de ciertas preparaciones como bollos, pasteles, magdalenas, etc. En la mayoría de los casos el fondant es una decoración repostera")
        print("Chantully se trata de una crema espesa y dulce. ")
        print("Creama Pastelera es una crema dulce ")
        print("El betún es una crema a base de mantequilla y azúcar.")
        decorationOps = input("La decoración que menciono: ¿la desea en fondant, en crema, betun, chantilly? ---> \t")
        if decorationOps == "fondant" or decorationOps == "crema" or decorationOps == "betun" or decorationOps == "chantilly":
            conlusion = conlusion + " y la decoración será: " + decorationOps
        else:
            conlusion = conlusion + " y la decoración será: " + decorationOps
        
    
    elif event == "día del padre":
        taste = input("¿De que sabor lo desea? ---> \t")
        if taste == "Recomiendeme uno" or taste == "Nose" or taste == "que sabor es comun para el día del padre":
            print("Los sabores que se dan comunmente para el día del padre son: cafe, cafe capuchino, moka, chocolate ")
            tasteOps = input("Entonces el sabor de su pastel será: ---> \t")
            conlusion = conlusion + ", el sabor del pastel será: " + tasteOps
        else :
            conlusion = conlusion + ", el sabor del pastel será: " + taste
        
        print("El pastel en pisos es un pastel escalonado donde lleva una base y sobre de ella otra pero más chica y así sucesivamente \n y en plancha es un pastel rectangulas o circular sin ninguna escala ") 
        cakeType = input("¿El pastel lo desea en pisos o en plancha? ---> \t")
        conlusion = conlusion + ", el pastel será en: " + cakeType
        
        decorationCake = input("Describe la decoración que desea que tenga el pastel: ---> \t")
        conlusion = conlusion + " y la decoración será: " + decorationCake
        
        print("================================")
        print("El fondant es una pasta parecida a la plastilina pero comestible, empleada como recubrimiento de ciertas preparaciones como bollos, pasteles, magdalenas, etc. En la mayoría de los casos el fondant es una decoración repostera")
        print("Chantully se trata de una crema espesa y dulce. ")
        print("Creama Pastelera es una crema dulce ")
        print("El betún es una crema a base de mantequilla y azúcar.")
        decorationOps = input("La decoración que menciono: ¿la desea en fondant, en crema, betun, chantilly? ---> \t")
        if decorationOps == "fondant" or decorationOps == "crema" or decorationOps == "betun" or decorationOps == "chantilly":
            conlusion = conlusion + " y la decoración será: " + decorationOps
        else:
            conlusion = conlusion + " y la decoración será: " + decorationOps
        
        
    elif event == "casual":
        taste = input("¿De que sabor lo desea? ---> \t")
        if taste == "Recomiendeme uno" or taste == "Nose" or taste == "que sabor es comun para algo casual":
            print("Los sabores que se dan comunmente para el algo casual: vainilla, 3 leches, chocolate, red velvet, naranja, marmoleado, cafe, moka, capuchino, naranja ")
            tasteOps = input("Entonces el sabor de su pastel será: ---> \t")
            conlusion = conlusion + ", el sabor del pastel será: " + tasteOps
        else :
            conlusion = conlusion + ", el sabor del pastel será: " + taste
        
        print("El pastel en pisos es un pastel escalonado donde lleva una base y sobre de ella otra pero más chica y así sucesivamente \n y en plancha es un pastel rectangulas o circular sin ninguna escala ") 
        cakeType = input("¿El pastel lo desea en pisos o en plancha? ---> \t")
        conlusion = conlusion + ", el pastel será en: " + cakeType
        
        decorationCake = input("Describe la decoración que desea que tenga el pastel: ---> \t")
        conlusion = conlusion + " y la decoración será: " + decorationCake
        
        print("================================")
        print("El fondant es una pasta parecida a la plastilina pero comestible, empleada como recubrimiento de ciertas preparaciones como bollos, pasteles, magdalenas, etc. En la mayoría de los casos el fondant es una decoración repostera")
        print("Chantully se trata de una crema espesa y dulce. ")
        print("Creama Pastelera es una crema dulce ")
        print("El betún es una crema a base de mantequilla y azúcar.")
        decorationOps = input("La decoración que menciono: ¿la desea en fondant, en crema, betun, chantilly? ---> \t")
        if decorationOps == "fondant" or decorationOps == "crema" or decorationOps == "betun" or decorationOps == "chantilly":
            conlusion = conlusion + " y la decoración será: " + decorationOps
        else:
            conlusion = conlusion + " y la decoración será: " + decorationOps
    
    date = input("Para que fecha necesita el pastel ---> \t")
    conlusion = conlusion + " es para: " + date
    
    address = input("¿Desea saber si se puede llevar a docimilio? ---> \t")
    if address == "si":
        print("Se puede llevar a docimilio el pastel pero este tiene un costo extra")
        goAddress = input("¿Desea que llevemos el pastel a su domicilio? ---> \t")
        if goAddress == "si":
            print("El precio por esto será de: 100" )
            conlusion = conlusion + " el precio del pastel será de: " + str(precio + 100)
            dataAddress = input("¿Cuál es su domicilio? ---> \t")
            conlusion = conlusion + " se llevará a docimilio y su direción es: " + dataAddress
        else: 
            conlusion = conlusion + " No se llevará a docimilio "
    else: 
        print("No se llevará a docimilio")
    
    
    
    itWantQuestion = input("Desea hacer alguna pregunta aparte de lo que ya se menciono ---> \t")
    while itWantQuestion == "si":
        question = input("¿Cual es su pregunta? ---> \t")
        if question == "¿El pan no es seco?":
            print("El pan no es seco")
        if question == "¿Se puede pasar antes por el pastel?":
            print("No, no se puede")
        if question == "¿Das prueba de pastel?":
            print("Si, pero tiene un costo extra")
            testCake = input("Desea la prueba de pastel ---> \t")
            conlusion = conlusion + " además, va a querer una prueba de pastel "
        if question == "¿A que hora estará listo?":
            print("En la fecha ya establecida")
        if question == "¿Lo puedes dejar más economico?":
            print("No, no se puede")
        if question == "¿El pan va relleno?":
            filledDecision = input("EL pastel puede tener relleno, ¿desea que le pongamos algun relleno? ---> \t")
            if filledDecision == "si":
                filled = input("Puede ser de fresas, durazno o cremaquilla ---> \t")
                conlusion = conlusion + " el pastel tendra un relleno de: " + filled
        if question == "¿Hacen sobrepedido para envetos grandes o solamente son los de exibicion?":
            print("De las dos formas que ha mencionado")
            
        itWantQuestion = input("¿Desea hacer alguna otra pregunta? ---> \t")
        
    dataClient = input("Me puede pasar sus datos por favor: \n Su nombre y telefono: ---> \t")
    conlusion = conlusion + " \n \n Los datos del cliente son: " + dataClient
    
    print("Para poder emepzar a realizar el pastel que encargo necesitamos un anticipo de 0.25 porciento")
    conlusion = f"{conlusion}  \n \n El anticipo es: {int(precio * 0.30)}"
    
    
    print("La conclusión es: \n" + conlusion + " \n el pago será de: ", precio)
    
else:
    print("No desea un pastel, gracias por su visita ");