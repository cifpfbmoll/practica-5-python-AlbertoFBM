# PRÁCTICA 5 --> EJERCICIO 12
# Escribe un programa que pida un número y escriba si primo o no.
# Dame un número: 123
# El número 123 no es primo
# Dame un número:127
# El número 127 es primo

print("Pon un número y te diré si es primo o no:")

numero= int(input("pon un número:"))

esPrimo = True

for i in range(numero):
    if ((i != 0) and (i != 1 ) and (numero%i==0)):
        esPrimo = False

if (esPrimo):
    print("El número", numero,"es primo")
else:
    print("El número", numero,"no es primo")