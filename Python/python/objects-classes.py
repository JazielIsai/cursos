#Python has lost of data types 
#Types:
#   int: 1,2,32,435,2354
#   float: 1.2, 0.435
#   string: "a", "abcd", "hola"
#   List: [ 1, 2, 'ab' ]
#   Dictionary: { "dog": 1, "cat": 2  }
#   Bool: False, True
# Each is an Object
# 

#Definimos nuestra clase
class Circle( object ): 

    #Data attributes used to initialize each instance of the class, the constructor
    #special method or constructor used to initialize data attributes
    #la funcion __init__ es un constructor
    #el parameto self se refiere a la instancia recién creada de la clase
    def __init__( self, radius, color ):
        self.radius = radius;
        self.color = color;

    def add_radius(self, r):
        self.radius =self.radius + r
    
    def drawCircles(self):
        pass



class Reactangle ( object ): 
    
    def __init__ (self, color, height, width):
        self.color = color;
        self.height = height;
        self.width = width;


#despues de crear la clase con el fin de crear un objeto de circulo de clase, vamos a instanciar la clase
#instanciar la clase
RedCircle = Circle(10, "red")
# RedCircle.radius #nos devolvería el valor
# print( RedCircle.radius )
# print( RedCircle.color )

# RedCircle.color = "blue"
# print( RedCircle.color )


print( RedCircle.radius )
RedCircle.add_radius(2)
print( RedCircle.radius )


#"La función dir() es util para conocer los argumentos o atributos y metodos que contene un objeto o clase"
print(dir(RedCircle))