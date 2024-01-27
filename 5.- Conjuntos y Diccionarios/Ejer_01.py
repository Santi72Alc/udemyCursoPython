"""
Ejercicio 1

Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

"""

dias2024 = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

mes = int(input("Introduzca mes: "))

if mes < 1 or mes > 12:
    print("El mes seleccionado NO existe, (Entre 1 y 12, por favor)")
else:
    print(f"El mes seleccionado: {mes} tiene {dias2024[mes-1]} días")
