
#           parametro1 = localización del archivo
#           parametro2 = "w" = escribir, "r" = leer,  "a" = agregar,

# file1 = open("")

# #Podemos ver en que módo se ecuentra el objeto usando el modo de atributo de datos
# file1.name # = direción o localización del archivo
# file1.mode # = "r", "w", "a"
# file1.close() #Siempre se debe cerrar el objeto de archivo utliziando el método close

# Usar una instrucción "with" para abrir un archivo es
with open("C:\Users\jhazy\Downloads\texto.text", "r") as file2:
    file_stuff = file2.read()
    print( file_stuff )
# print( file2.close() )
# print(file_stuff)

# el metodo readline es para leer linea por linea
with open("C:\Users\jhazy\Downloads\texto.text", "r") as file2:
    file_stuff = file2.readline()
    print( file_stuff )

# podemos usar un bucle para imprir
with open("example.txt", "r") as File2:
    for line in File2:
        print( line )
