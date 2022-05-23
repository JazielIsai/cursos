from inspect import getfile


try:
    getfile = open('myfile', "r")
    getfile.write("file for exception handling.")
except IOError:
    print("Unable to open or read the data in the file.")
