# PRÁCTICA 5 --> EJERCICIO 4
# Escribe un programa que pida un número y calcule su factorial.

numero = int(input("Dame un número para calcular su factorial: "))

if(numero == 0):
    print(f"El factorial de {numero} es 1")
else:
    factorial = 1 #Habia puesto 0 pero numero *0 es 0 :(
    for i in range(1,numero+1):
        factorial = factorial * i
    print(f"El factorial de {numero} es {factorial}")