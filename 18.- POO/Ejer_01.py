"""
Ejercicio 1

Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def isAprobado(self):
        return self.nota > 5

    def estado(self):
        if self.isAprobado():
            print(f"El alumno {self.nombre} está aprobado con un {self.nota}")
        else:
            print(f"El alumno {self.nombre} está suspendido con un {self.nota}")



pedro = Estudiante("Pedro", 6.5)
pedro.estado()

juan = Estudiante("Juan", 3)
juan.estado()