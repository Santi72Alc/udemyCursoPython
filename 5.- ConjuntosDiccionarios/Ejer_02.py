"""
Ejercicio 2

Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa

"""

letras = ("A", "Be", "Ce", "De", "E", "Efe", "Ge", "Hache (H)", "I", "Jota", "Ka", "Ele", "Eme", "Ene", "Eñe",
          "O", "Pe", "Cu (Q)", "Erre, Ere (R)", "Ese", "Te", "U", "Uve", "Uve-doble", "Equis (X)", "I-Griega (Y)", "Zeta")

print(f"Total de letras en el abecedario: {len(letras)} letras")

numLetra = int(input(f"Introduzca num. de posición (1-{len(letras)}): "))

if numLetra < 1 or numLetra > len(letras):
    print("El letra seleccionado NO es del abecedario, (Entre 1 'A' y 26 'Z', por favor)")
else:
    print(f"La letra seleccionada es la {numLetra}: {letras[numLetra-1]}")