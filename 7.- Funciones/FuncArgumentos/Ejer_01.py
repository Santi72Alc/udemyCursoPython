"""
Ejercicio 1

Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio
"""

def cuadrado( base=0, altura=0):
    if base<=0 or altura<=0:
        print("Error de parámetros")
        return
    
    print(f"CUADRADO con base={base}cms y altura={altura}cms y tiene área={base*altura:.4f}")


def circulo(radio=0):
    from math import pi
    if radio<=0:
        print("Error de parámetro")
        return
    print(f"El área del círculo con radio: {radio}cms es {pi*radio**2:.4f}")


# Prueba
cuadrado(5,2)
circulo(3)