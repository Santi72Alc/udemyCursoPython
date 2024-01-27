"""
Ejercicio 2

Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""

def myFactorial():
    from math import factorial
    print("IMPRIMIR EL FACTORIAL")
    num = int(input(f"Numero (> 0): "))

    return factorial(num)


# Prueba
print(f"Calculo del factorial: {myFactorial()}")
