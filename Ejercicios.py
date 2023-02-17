"""--------- Ejercicio 10 -----------"""

# En su casa le solicitan que realice un algoritmo en Python,
# que permita calcular el valor a pagar por concepto de
# energía eléctrica. Los datos que se conocen son los
# siguientes:

# estrato
# - Mes de consumo
# Valor kw
# -Total kw consumido en el mes 

# 656,34 pesos colombianos por kWh

kh = 656.34
salir = exit

descuento1 = 16.486
descuento2 = 12.256
descuento3 = 6.342

print(f"    --------------------------------------------------")
print(f"\t    1. Ingresar ingresar al sistema \n \t\t\t2. Salir")
print(f"    --------------------------------------------------")
ingreso = int(input(f"\t\t\t    "))


if ingreso == 1:
    print(f"    ------------------------------------------------------")
    print("    El valor de kilowatts/h es de 656,34 pesos colombianos")
    print(f"    ------------------------------------------------------")
    
    
    print(f"    ---------------------")
    estrato = int(input("    -> Digite su estrato: "))
    print(f"    ---------------------")
    
    if estrato == 1:

        print(f"    -------------------------------------------")
        mes = (input("    -> Escriba el mes en que se facturo el recibo: "))
        print(f"    -------------------------------------------")
    
        print(f"    -----------------------------------------------")
        K = int(input("    -> Digite cuantos kilowatts consumio en el mes: "))
        print(f"    -----------------------------------------------")


        costo = kh * K - descuento1

        print(f"    ------------------------------------------------------------------")
        print(f"         Por ser estrato 1 usted obtiene un descuento de ${descuento1} pesos")
        total = print(f"          -> El total a pagar en el mes de {mes} es de ${costo:.2f}")
        print(f"    ------------------------------------------------------------------")
        
    elif estrato == 2:
        
        print(f"    -------------------------------------------")
        mes = (input("    -> Escriba el mes en que se facturo el recibo: "))
        print(f"    -------------------------------------------")

        print(f"    -----------------------------------------------")
        K = int(input("    -> Digite cuantos kilowatts consumio en el mes: "))
        print(f"    -----------------------------------------------")

        costo = kh * K - descuento2

        print(f"    ------------------------------------------------------------------")
        print(f"         Por ser estrato 2 usted obtiene un descuento de ${descuento2} pesos")
        total = print(f"          -> El total a pagar en el mes de {mes} es de ${costo:.2f}")
        print(f"    ------------------------------------------------------------------")
        
    elif estrato == 3:

        print(f"    -------------------------------------------")
        mes = (input("    -> Escriba el mes en que se facturo el recibo: "))
        print(f"    -------------------------------------------")

        print(f"    -----------------------------------------------")
        K = int(input("    -> Digite cuantos kilowatts consumio en el mes: "))
        print(f"    -----------------------------------------------")

        costo = kh * K - descuento3

        print(f"    ------------------------------------------------------------------")
        print(f"         Por ser estrato 3 usted obtiene un descuento de ${descuento3} pesos")
        total = print(f"          -> El total a pagar en el mes de {mes} es de ${costo:.2f}")
        print(f"    ------------------------------------------------------------------")
            
    elif estrato == 4:
    
        print(f"    -------------------------------------------")
        mes = (input("    -> Escriba el mes en que se facturo el recibo: "))
        print(f"    -------------------------------------------")
        
        print(f"    -----------------------------------------------")
        K = int(input("    -> Digite cuantos kilowatts consumio en el mes: "))
        print(f"    -----------------------------------------------")

        costo = kh * K

        print(f"    ------------------------------------------------------------------")
        total = print(f"          -> El total a pagar en el mes de {mes} es de ${costo:.2f}")
        print(f"    ------------------------------------------------------------------")
        
    elif estrato == 5:
        
        print(f"    -------------------------------------------")
        mes = (input("    -> Escriba el mes en que se facturo el recibo: "))
        print(f"    -------------------------------------------")

        print(f"    -----------------------------------------------")
        K = int(input("    -> Digite cuantos kilowatts consumio en el mes: "))
        print(f"    -----------------------------------------------")

        costo = kh * K

        print(f"    ------------------------------------------------------------------")
        total = print(f"          -> El total a pagar en el mes de {mes} es de ${costo:.2f}")
        print(f"    ------------------------------------------------------------------")
        
    elif estrato == 6:
        
        print(f"    -------------------------------------------")
        mes = (input("    -> Escriba el mes en que se facturo el recibo: "))
        print(f"    -------------------------------------------")

        print(f"    -----------------------------------------------")
        K = int(input("    -> Digite cuantos kilowatts consumio en el mes: "))
        print(f"    -----------------------------------------------")

        costo = kh * K

        print(f"    ------------------------------------------------------------------")
        total = print(f"          -> El total a pagar en el mes de {mes} es de ${costo:.2f}")
        print(f"    ------------------------------------------------------------------")
        
    else: 
        print("Solo hay hasta estrato nivel 6")

elif ingreso == 2:
    print(salir)
else: 
    print("El dato no es valido")

""" ------------------------------- """