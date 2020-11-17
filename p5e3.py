# PRÁCTICA 5 --> EJERCICIO 3
# Escribe un programa que pida dos números y escriba la suma
# de enteros desde el primero hasta el último.

print("Escriba dos números y le daré la suma desde el primero \n\
    hasta el último: ")
numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))
suma = 0

for i in range(numero1, numero2 +1):
    suma = suma + i
print(f"La suma desde {numero1} hasta {numero2} = {suma}")
ver_suma = input("Quieres ver la suma? ")
if(ver_suma == "Si") or (ver_suma == "si") or (ver_suma == "SI"):
    for i in range(numero1, numero2):
        print(f"{i} + ", end = "")
    print(f"{numero2} = {suma}")
else:
    print("Ok")