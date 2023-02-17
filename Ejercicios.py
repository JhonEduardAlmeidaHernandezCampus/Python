"""--------- Ejercicio 8 -----------"""

#Escriba un bloque cualquiera de código en Python en donde utilice 2 condicionales (if) anidados.

edad = int(input("Escribe tu edad: "))
grupo = input("Escribe a que grupo quieres pertenecer [A o B]: ")

if edad >= 18 and grupo == "A" or grupo == "B":
	print(f"Puedes entrar al grupo {grupo}")
elif edad < 18 and grupo == "A" or grupo == "B":
	print(f"No puedes entrar al grupo {grupo} si eres menor de edad")
else:
	print("Elección no válida")

""" ------------------------------- """