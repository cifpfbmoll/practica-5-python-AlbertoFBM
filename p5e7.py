# PRÁCTICA 5 --> EJERCICIO 7
# Escribe un programa que pida la altura de un triángulo 
# y lo dibuje de la siguiente manera:

# ****
# ***
# **
# *

altura = int(input("Ponga la altura del triángulo: "))

for i in range(altura,0,-1):
    print(i*"X")
    print(" ")