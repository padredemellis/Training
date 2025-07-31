'''
📝 Mini-Ejercicio 1: Clases Básicas
Objetivo: Comprender cómo crear clases con atributos y métodos.

Instrucciones:

Crea una clase llamada Persona con atributos nombre y edad
Añade un método __init__ para inicializar los atributos
Añade un método presentarse() que devuelva un string con la información de la persona
Crea dos instancias diferentes de la clase y haz que se presenten
'''
class Persona:
    def __init__(self, name: str, edad:int) -> None:
        self.name = name
        self.edad = edad
    
    def presentarse(self)->str:
        return f'Hola soy {self.name} y tengo {self.edad}'
if __name__ == '__main__':
    fulano = Persona('Fulano', 15).presentarse()
    mengano = Persona('Mengano', 16).presentarse()
    print(fulano)
    print(mengano)