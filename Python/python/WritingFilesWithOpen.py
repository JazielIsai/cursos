#"Crear el ejemplo dos de la siguiente manera"

# Write line to file
exmp2 = 'Example2.txt'
# with open(exmp2, 'w') as writefile:
#     writefile.write("This is line A\n")
#     writefile.write("This is line B")

#Writing Files with open
# Lines = [ "This is line A\n", "This is line B\n", "This is line C\n", "This is line D"]
# with open(exmp2, 'w') as file1:
#     for line in Lines:
#         file1.write(line)

#leemos un archivo.tex primero, para que despues lo podamos copiar
exmp3 = 'Example3.text'
with open(exmp2, 'r') as readFile:

    with open(exmp3, 'w') as writingFile:

        for line in readFile:
            writingFile.write(line)