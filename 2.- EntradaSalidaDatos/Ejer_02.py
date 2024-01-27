"""
Ejercicio 2

Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final
"""


def parcial(notasPracticas = [], examenParcial = 0, examenFinal = 0):
    print("\n\n*** Promedio de un alumno\n")

    proPracticas = (notasPracticas[0] + notasPracticas[1] + notasPracticas[2]) / 3
    total = (proPracticas + (2*examenParcial) + (3*examenFinal)) / 6

    print(f"Con parcial en prácticas: {proPracticas:.0f} con las notas: {notasPracticas}")
    print(f"Con x2 del examen parcial: {examenParcial}")
    print(f"Con x3 del examen final: {examenFinal}")
    print(f"El alumno ha sacado un total (redondeado sin decimales): {total:.0f}")
    print("Calculado con (promedioPracticas + 2*examenParcial + 3*examenFila)")


# Prueba
parcial([6, 7, 8], 8, 7)
parcial([5, 5, 4], 7, 9)
    