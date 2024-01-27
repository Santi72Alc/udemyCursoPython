"""
Ejercicio 1

Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0
"""

def numMayor():
    num1 = input("1er número: ")
    num2 = input("2do número: ")

    if not num1 or 0 < int(num1) > 100:
        num1 = int(num1)
        num1 = 0
    if not num2 or 0 < int(num2) > 100:
        num2 = 0
        num2 = int(num2)
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0


# Prueba
print(f"Retornado: {numMayor()}")