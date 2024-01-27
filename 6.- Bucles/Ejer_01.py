"""
Ejercicio 1

Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

"""

print("LAS TABLAS DE MULTIPLICAR (del 1 al 10)")

numero = int(input("De qué número quiere? "))+1

if numero > 25 or numero < 1:
    print(f"El número pedido es demasiado!!!")

for n in range(1, numero):
    print(f"\nLa tabla del {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")