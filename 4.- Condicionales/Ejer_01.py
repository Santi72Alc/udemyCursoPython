"""
Ejercicio 1

Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

"""


def vocal():
    vocal = input("Introduzca vocal: ")[0]
    vocales = ["a", "e", "i", "o", "u"]

    if vocal.lower() in vocales:
        print(f"Lo introducido: {vocal} es una vocal")
    else:
        print(f"Lo introducido: {vocal} NO es una vocal")


# Prueba
vocal()