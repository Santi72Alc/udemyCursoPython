"""
Ejercicio 2

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

print("AÑOS CUMPLIDOS")

edad = int(input("Ingrese su edad: "))
anyoActual = 2024
nacio = anyoActual-edad
 
for a in range(nacio, anyoActual+1):
    if a==anyoActual:
        print(f"{a} - Hoy")
    elif a > nacio:
        print(f"{a}")
    else:
        print(f"{a} - Naciste") 

