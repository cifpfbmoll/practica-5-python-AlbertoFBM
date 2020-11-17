# PRÁCTICA 5 --> EJERCICIO 9
# Escribe un programa que pida la anchura y la altura de un rectángulo
# y lo dibuje de la siguiente manera:

# *****
# *   *
# *   *
# *****

anchura = int(input("Ponga la anchura de su rectángulo: "))
altura = int(input("Ponga la altura de su rectángulo: "))

for i in range(anchura):
    print("X", end=" ")

for i in range(altura-2):
    print("\nX", end=" ")
    for j in range(anchura-2):
        print(" ", end=" ")
    print("X", end=" ")

print(" ")

for i in range(anchura):
    print("X", end=" ")