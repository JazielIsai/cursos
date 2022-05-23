#functions

def function(a):
    #add 1 to a
    b = a + 1;

    print(a, " + 1 = ", b)
    return b


print(function(2))

# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

square(2)

def noWork():
    pass


# Make a Function for the calculation above
def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 


#El asterisco en un argumento hace que podamos enviar la información que deseemos y esta la convuerta en una tupla
def ArtistName(*names):
    for name in names:
        print(name)

ArtistName( 'Michel', 'Jonson', 'ABCD' )

def globales():
    global saludo
    saludo = "hola"
    return saludo

globales()
print(saludo)