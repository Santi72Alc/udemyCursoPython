"""
Ejercicio 1

Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

"""

class Fabrica():
    def __init__(self, llantas, color, precio) -> None:
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def __str__(self) -> str:
        str = f"El vehículo tiene {self.llantas} ruedas, es de color {self.color} y vale: {self.precio}€"
        return str

class Moto(Fabrica):
    def __init__(self, color, precio) -> None:
        super().__init__(2, color, precio)

class Carro(Fabrica):
    def __init__(self, color, precio) -> None:
        super().__init__(4, color, precio)


myMoto = Moto("Blanco", 10400)
myCarro = Carro("Azul", 34200)

print("Mi moto: ", myMoto)
print("Mi carro: ", myCarro)