"""
Ejercicio 1

Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.


"""

palabra1 = input("Introduzca 1ra palabra: ").lower()
palabra2 = input("Introduzca 2da palabra: ").lower()

if len(palabra1) < 3 or len(palabra2) < 3:
    print("Las palabras son muy cortas, y no riman")
elif palabra1.endswith(palabra2[-3:]):
    print("Riman perfectamente")
elif palabra1.endswith(palabra2[-2:]):
    print("Riman un poco")
else:
    print("NO riman nada")
    