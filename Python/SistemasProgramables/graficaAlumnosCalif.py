import matplotlib.pyplot as plt

n= int(input("ingrese la cantidad de alumnos \n"))
print(n)

Nombres= []
Calificaiones= []

for x range(n):
    nom= input("nombre del alumno: ")
    Nombres.append(nom)
    cal= int(input("calificaciones: "))
    calificaciones.append(cal)
    
print(Nombres)
print(Calificaciones)

fig= plt.figure()
ax= fig.add_subplot(111)

#alumnos= ["Hugo", "Paco", "Luis", "Diana", "Jorge"]
datos= [2,4,6,8,10]
xx= range(1,len(Calificaciones)+1)
