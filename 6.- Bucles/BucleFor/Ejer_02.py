"""
Ejercicio 2

Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares
"""

num1 = int(input("Ingrese número 1: "))
num2 = int(input("Ingrese número 2: "))
rango = abs(num1-num2)
print(f"Rango entre los numero introducidos ({num1} y {num2}) es {rango}")
print(f"Imprimo sólo impares entre 1 y {rango}")
for n in range(1, rango+1):
    if n%2 != 0:
        print(n)