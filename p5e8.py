# PRÁCTICA 5 --> EJERCICIO 8
# Escribe un programa que pida la anchura de un triángulo 
# y lo dibuje de la siguiente manera:

# *
# **
# ***
# ****
# ***
# **
# *

anchura = int(input("ponga la anchura del triángulo: "))

for i in range(anchura):
    print(i*"X")
    print(" ")
for i in list(range(anchura,0,-1)):
    print(i*"X")
    print(" ")
