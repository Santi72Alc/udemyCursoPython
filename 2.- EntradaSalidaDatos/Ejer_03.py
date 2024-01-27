"""
Ejercicio 1

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

"""

def vocal():
    vMin = input("Introduzca una letra (se pasará minúscula): ").lower()
    vMay = input("Introduzca una letra (se pasará mayúscula): ").upper()

    if not vMin or not vMay:
        print("Debe introducir los dos valores")
        return
    
    print(f"Se ha introducido {vMin[0]}{vMay[0]}")


# Prueba
vocal()