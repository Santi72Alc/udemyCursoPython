"""
Ejercicio 2

Escribir una función que reciba una muestra de números en una lista y devuelva su medida.
"""

def medida(*lista):
    longitudParam = len(lista)
    print(f"Longitud de introducido es {longitudParam}")
    return longitudParam


# Prueba
medida(23,3,4,"Hola", "adios", 5)