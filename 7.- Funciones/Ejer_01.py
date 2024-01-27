"""
Ejercicio 1

Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas
"""


def sumarALista():
    
    lista = []
    num = 99
    while num != 0:
        
        num = input("Introduzca lista (sólo números entre 1..100, INTRO - salir ): ")
        if num == "":   # Se ha pulsado INTRO
            num = 0
        num = int(num)  # Lo convertimos en numerico
        if num > 0 and num <= 100:
            lista.append(num)
        elif num != 0:
            print(f"{num} - Error de número")
    lista.sort()  # La ordenamos y la devolvemos
    return lista

def paresOrd(lista):
    newLista = []
    for n in lista:
        if n % 2 == 0:
            newLista.append(n)
    return newLista

def imparesOrd(lista):
    newLista = []
    for n in lista:
        if n % 2 != 0:
            newLista.append(n)
    return newLista

# Prueba
lista = sumarALista()
print(type(lista))
print(f"La lista: {lista}")

print(f"Impares...{imparesOrd(lista)}")
print(f"Pares...{paresOrd(lista)}")
