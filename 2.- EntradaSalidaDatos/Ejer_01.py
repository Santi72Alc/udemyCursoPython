"""
Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”

        x = (-b +-sqr(b²-4ac))/2a)
"""
from math import sqrt


def ecuacion():
    print("Cálculo de funciones. Valores será a, b y c")
    a = int(input("Introduzca valor para a: "))
    b = int(input("Introduzca valor para b: "))
    c = int(input("Introduzca valor para c: "))

    baseRaiz = (b**2)-(4*a*c)
    if baseRaiz < 0:
        print("No se pueden calcular raices de números negativos")
        return
    
    resultadoPos = (-b + sqrt(baseRaiz)) / (2*a)
    resultadoNeg = (-b - sqrt(baseRaiz)) / (2*a)
    print(f"1ro de los resultados es : {resultadoPos}")
    print(f"2do de los resultados es : {resultadoNeg}")



# Prueba
ecuacion()