tipoOperation = input("Elije el tipo de opeación que desee realizar: ")
valor1 = input("Ingresa el valor 1: ")
valor2 = input("Ingresa el valor 2: ")

if tipoOperation.upper() == "SUMA":
    print(valor1 + valor2)
elif tipoOperation.upper() == "RESTA":
    print(valor1 - valor2)
elif tipoOperation.upper() == "MULTIPLICACION":
    print(valor1 * valor2)

elif tipoOperation.upper() == "DIVISION":
    print(valor1 / valor2)
else:
    print("ingresa una operacion valida")

temperatura = float(input("Danos tu temperatura: "))

if temperatura < 35:
    print("Hipotermia")
elif temperatura > 36.8:
    print("fiebre")
else:
    print("temperatura normal")
