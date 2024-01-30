"""
Ejercicio 1

Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
"""

class Calculadora():
    def __init__(self):
        self.noOperar = False
        self.num1 = int(input("Introduzca 1er valor (0 - salir): "))
        if self.num1 == 0:
            print("Salimos...")
            self.noOperar = True
            return
        else:
            self.num2 = int(input("Introduzca 2do valor: "))

    def sumar(self):
        return self.num1 + self.num2 if not self.noOperar else False
    
    def restar(self):
        return self.num1 - self.num2 if not self.noOperar else False

    def multiplicar(self):
        return self.num1 * self.num2 if not self.noOperar else False

    def dividir(self):
        return self.num1 / self.num2 if not self.noOperar else False


oper = Calculadora()


print("Sumamos: ", oper.sumar())
print("Restamos: ", oper.restar())
print("Multiplicamos: ", oper.multiplicar())
print("Dividimos: ", oper.dividir())

