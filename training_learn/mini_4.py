'''
Objetivo: Entender el concepto de clases y métodos abstractos.

Instrucciones:

Importa el módulo abc para crear clases abstractas
Crea una clase abstracta FiguraGeometrica con métodos abstractos calcular_area() y calcular_perimetro()
Crea dos clases concretas: Rectangulo y Circulo que hereden de FiguraGeometrica
Implementa los métodos abstractos en cada clase
Verifica que no puedes instanciar directamente FiguraGeometrica pero sí las clases concretas
'''
from abc import ABC, abstractmethod
from math import pi

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return  pi * (self.radio ** 2) 
    
    def calcular_perimetro(self):
        return 2 * pi * self.radio

if __name__ == '__main__':
    cuadrado = Rectangulo(2,2)
    cuadrado.calcular_area()
    cuadrado.calcular_perimetro()
    redondo = Circulo(5)
    redondo.calcular_area()
    redondo.calcular_perimetro()