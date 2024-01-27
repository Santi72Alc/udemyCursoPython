"""
Ejercicio 2

Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula
"""

candidato = input("Introduzca candidato (A/B/C): ")[0].upper()

if candidato == "A":
    print(F"Elegiste: {candidato}. El partido rojo")
elif candidato == "B":
    print(F"Elegiste: {candidato}. El partido verde")
elif candidato == "C":
    print(F"Elegiste: {candidato}. El partido azul")
else:
    print("Elección errónea")
