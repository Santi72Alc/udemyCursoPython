"""
Ejercicio 2

Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0.
"""


def intercalar(cadena="", caracter= ','):
    print(f"Cadena original: {cadena}")

    l = 0
    longitudCad = len(cadena)-1
    
    while l <= longitudCad:
        print(f"{cadena[l]}", end="")
        if l < longitudCad:
            print(f"{caracter}", end="")
        l += 1
    print()

 
# Prueba
intercalar("separar", ",")