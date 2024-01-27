"""
Ejercicio 1

Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras
"""
print("Números entre 1 y 10")
for n in range(1, 11):
    print(n)


num1 = int(input("Ingrese número 1 (entre 1 y 10): "))
num2 = int(input("Ingrese número 2 (entre 1 y 10): "))
rango = num1-num2

if num1 < 1 or num1 > 10 or num2 < 0 or num2 > 10:
    print("Algún número introducido no es correcto")
else:
    for n in range(num1, num2+1):
        print(n)