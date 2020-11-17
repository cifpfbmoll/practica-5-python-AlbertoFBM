# PRÁCTICA --> EJERCICIO 10
# Escribe un programa que pida la altura de un triángulo
# y lo dibuje de la siguiente manera:

#     *
#    ***
#   *****
#  *******
# *********

altura = int(input("Ponga la altura del triángulo: "))

for i in range(altura):
    if (i==altura-1):
        print(" "+((i*2)+1)*"*")
    else:
        print((" "*(altura-i))+(((i*2)+1)*"*"))