""" ------- Skill Review Funciones ------- """

""" ---------- Ejercicio 1 ----------- """

#1. Campus requiere administrar algunos datos de sus Campers
#como por ejemplo, la creación, eliminación o búsqueda de los
#developers, entre otros, por tal razón, ha solicitado el diseño de
#un programa que cuente con el siguiente menú como panel de
#control:

# 1. CREAR GRUPO ARTEMIS:
# 1.1 LISTAR CAMPERS DE ARTEMIS 
# 1.2 AGREGAR CAMPERS A ARTEMIS 
# 1.3 ELIMINAR CAMPERS DE ARTEMIS
# 1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS
# 1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS
# 2. CREAR GRUPO SPUTNIK:
# 2.1 LISTAR CAMPERS DE SPUTNIK
# 2.2 AGREGAR CAMPERS A SPUTNIK
# 2.3 ELIMINAR CAMPERS DE SPUTNIK
# 2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK
# 2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK
# Digite opcion:

grupo1 = "Artemis"
lista = ["Manuel", "Santiago", "Ricardo", "Sofia", "Samuel", "Antonio", "Carmen"]
lista2 = ["Fabian", "Miguel", "Mariana", "Jessica", "Samuel", "Carlos", "Silvia"]
grupo2 = "Sputnik"

print(f"-------------------------------- MENU -----------------------------------")
print(f"|\t\t\t\t\t\t\t\t\t|")
print(f"|\t-> 1. CREAR GRUPO ARTEMIS: \t\t\t\t\t|\n|\t-> 1.1 LISTAR CAMPERS DE ARTEMIS: \t\t\t\t|\n|\t-> 1.2 AGREGAR CAMPERS A ARTEMIS: \t\t\t\t|\n|\t-> 1.3 ELIMINAR CAMPERS DE ARTEMIS: \t\t\t\t| \n|\t-> 1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS: \t\t|\n|\t-> 1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS: \t\t\t|\n|\t-> 2. CREAR GRUPO SPUTNIK: \t\t\t\t\t|\n|\t-> 2.1 LISTAR CAMPERS DE SPUTNIK: \t\t\t\t| \n|\t-> 2.2 AGREGAR CAMPERS A SPUTNIK: \t\t\t\t|\n|\t-> 2.3 ELIMINAR CAMPERS DE SPUTNIK \t\t\t\t|\n|\t-> 2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK \t\t|\n|\t-> 2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK \t\t\t|\n|\t\t\t\t\t\t\t\t\t|")

opciones = float(input(f"|\t-> Digite una opción: \t\t\t\t\t\t| \n------------------------------------------------------------------------- \n|\t-> "))

if opciones == 1:
    print(f"\t ° El grupo {grupo1} ha sido creado satisfactoriamente")

elif opciones == 1.1:
    print(f"\t ° {lista}")

elif opciones == 1.2:
    agregar = input(f"\t ° Digite el nombre que quiere agregar a la lista de Artemis: ")
    lista.append(agregar)
    print(f"\t ° El listado de Artemis consta de los siguientes integrantes: {lista}")

elif opciones == 1.3:
    eliminar = int(input(f"\t ° Digite el ID del camper que se encuentra en Artemis que quiere eliminar: "))
    lista.pop(eliminar)
    print(f"\t ° El listado de Artemis consta de los siguientes integrantes: {lista}")

elif opciones == 1.4:
    lista.sort()
    print(f"\t ° El listado de Artemis quedo ordenado de la siguiente manera: {lista}")

elif opciones == 1.5:
    buscar = int(input(f"\t ° Digite el ID del camper que se encuentra en Artemis que quiere buscar: "))
    print(f"\t ° El camper de Artemis con ese ID es: {lista[buscar]}")

if opciones == 2:
    print(f"\t ° El grupo {grupo2} ha sido creado satisfactoriamente")

elif opciones == 2.1:
    print(f"\t ° {lista2}")

elif opciones == 2.2:
    agregar = input(f"\t ° Digite el nombre que quiere agregar a la lista de Sputnik: ")
    lista2.append(agregar)
    print(f"\t ° El listado de Sputnik consta de los siguientes integrantes: {lista2}")

elif opciones == 2.3:
    eliminar = int(input(f"\t ° Digite el ID del camper que se encuentra en Sputnik que quiere eliminar: "))
    lista2.pop(eliminar)
    print(f"\t ° El listado de Sputnik consta de los siguientes integrantes: {lista2}")

elif opciones == 2.4:
    lista2.sort()
    print(f"\t ° El listado de Sputnik quedo ordenado de la siguiente manera: {lista2}")

elif opciones == 2.5:
    buscar = int(input(f"\t ° Digite el ID del camper que se encuentra en Sputnik que quiere buscar: "))
    print(f"\t ° El camper de Sputnik con ese ID es: {lista2[buscar]}")

else:
    print(f"\t ° Esta opción no es valida")

""" ---------------------------------- """