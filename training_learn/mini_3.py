#!/usr/bin/python3
'''
Objetivo: Practicar la herencia de clases.

Instrucciones:

Crea una clase base Animal con atributos nombre y edad
Añade un método hacer_sonido() que devuelva "Sonido genérico"
Crea dos clases derivadas: Perro y Gato que hereden de Animal
Cada clase derivada debe sobrescribir hacer_sonido() con su sonido característico
Añade un atributo específico para cada clase derivada (por ejemplo, raza para Perro)
Prueba crear instancias y llamar a los métodos
'''
class Animal:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self)->str:
        return "Sonido genérico"

class Perro(Animal):
    def __init__(self, nombre: str, edad: int, raza: str) -> None:
        super().__init__(nombre, edad)
        self.raza = raza
        
    def hacer_sonido(self) -> str:
        return "Woof!"
    
class Gato(Animal):
    def __init__(self, nombre: str, edad: int, raza: str) -> None:
        super().__init__(nombre, edad)
        self.raza = raza
        
    def hacer_sonido(self) -> str:
        return "Miau!"

if __name__ == '__main__':
    firulais = Perro('Firulais', 2, 'Grandanés')
    gatomon = Gato('Gatomon', 1, 'Digimon')

    print(firulais.hacer_sonido())
    print(gatomon.hacer_sonido())
