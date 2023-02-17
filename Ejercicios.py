"""--------- Ejercicio 9 -----------"""

# Construya un algoritmo en Python, que permita ingresar la
# información de un empleado e imprima el nombre, los apellidos y la antigüedad. 
# Los datos que se deben solicitar
# son los siguientes:
#* Nombre 
#* Teléfono 
#* Año de ingreso a la empresa
#* Apellidos 
#* Edad.

nombre = input("Digite su nombre ")
apellido = input("Digite su apellido ")
edad = input("Digite su edad ")
telefono = int(input("Digite su numero de teléfono "))
ingreso = int(input("Digite el año en el que ingreso a la empresa "))
actual = 2023
antiguedad = actual - ingreso

if ingreso <= 2022:
    print("Su nombre es ", nombre, apellido, "Y lleva ", antiguedad, " años en la empresa")
elif ingreso == 2023:
    print("Su nombre es ", nombre, apellido, "Y lleva menos de un año en la empresa")
else:
    print("Año en el que ingreso a la empresa incorrecto")

""" ------------------------------- """