# PRÁCTICA 5 --> EJERCICIO 2
# Escribe un programa que pida dos números y escriba qué números entre
# ese par de números son pares y cuáles impares.

print("Pon 2 números y te diré si son pares e impares, además de los \n\
que están entre ellos.")
numero1 = int(input("Ponga el primer número: "))
numero2 = int(input(f"Ponga un número mayor que {numero1}:"))

if(numero2<numero1):
    print("He dicho que el segundo sea mayor que el primero...")
else:
    for numeros in range(numero1,numero2 +1):
        if (numeros % 2 == 0):
            print(numeros," es par")
        else:
            print(numeros," es impar")

