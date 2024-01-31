"""
Ejercicio 2

Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

{

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}
"""

jugadores = {
    1 : "Casillas", 15 : "Ramos", 3 : "Pique", 5 : "Puyol", 11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"
}


while True:
    numJugador = int(input("Qué número de jugador quieres saber (-1 - Salir)? "))
    try:
        if numJugador == -1:
            break
        nombre = jugadores.get(numJugador)
        if nombre != None:
            print(f"El jugador número {numJugador} es: {nombre}")
        else:
            print("Jugador NO conocido")
    except:
        print("Error en entrada")
