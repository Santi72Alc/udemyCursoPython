"""
Ejercicio 1

Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.

"""

def infoString():
    cadena = "Te quiero solo como amigo"

    print(f"Cadena ORIGINAL: {cadena}")
    print(f"\nLos 3 primeros caracteres. '{cadena[0]}{cadena[1]}{cadena[2]}'")

    print(f"\nLos 3 últimos caracteres. '{cadena[-3]}{cadena[-2]}{cadena[-1]}'")

    print(f"\nCadena impresa cada 2 caracteres. ", end="")
    for i in range(0, len(cadena), 2) :
        print(cadena[i], end="")

    print(f"\nCadena: {cadena}. Es en invertida: ", end="")
    i = len(cadena)-1
    while i >= 0:
        print(cadena[i], end="")
        i -= 1
    print()

# Prueba
infoString()