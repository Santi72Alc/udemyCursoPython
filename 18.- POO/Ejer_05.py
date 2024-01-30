"""
Ejercicio 1

Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
"""

class Universidad():
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Carrera():
    def __init__(self, especialidad) -> None:
        self.carrera = especialidad

class Estudiante(Universidad, Carrera):
    def  __init__(self, nombre, edad, universidad, carrera) -> None:
        self.nombre = nombre
        self.edad = edad
        self.universidad = Universidad(universidad).nombre
        self.carrera = Carrera(carrera).carrera

    def __str__(self) -> str:
        return f"Soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera} en la universidad {self.universidad}"

persona = Estudiante("Santi", 38, "UA", "Ciencias Físicas")
print(persona)