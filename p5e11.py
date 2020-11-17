# PRÁCTICA 5 --> EJERCICIO 11
# Escribe un programa que pida un número e imprima todos sus divisores.

print("Dame un número y te diré todos sus divisores.")

numero = int(input("Dime el número: "))

for i in range(numero+1):
    if ((i!=0)and(numero%i==0)):
        print(i, end=", ")
