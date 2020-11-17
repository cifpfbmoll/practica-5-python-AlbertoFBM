# PRÁCTICA 5 --> EJERCICIO 5
# Escribe un programa que pida la altura y ancho de un rectángulo 
# y lo dibuje de la siguiente manera:

# *****
# *****
# *****

print("Escultor de rectángulos")
ancho = int(input("escriba la anchura del rectángulo: "))
alto = int(input("escriba la altura del rectángulo: "))

for i in range(alto):
    i = " "
    for j in range(ancho):
        j= "X"
        print(j, end=" ")
    print(i)