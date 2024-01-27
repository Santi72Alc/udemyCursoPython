"""
Ejercicio 2

Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>


"""

def pedirDatos():

    nombre = input("Introduzca nombre: ")
    edad = int(input("Introduzca edad: "))
    sexo = input("Introduzca sexo: ")
    
    print(f"Te llamas: {nombre}")
    print(f"Tu edad: {edad}")
    print(f"Eres: {sexo}")


pedirDatos()