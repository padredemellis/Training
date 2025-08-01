'''
Objetivo: Aprender a convertir objetos a diccionarios.

Instrucciones:

Crea una clase Estudiante con atributos nombre, edad y calificaciones (lista)
Implementa un método to_dict() que devuelva un diccionario con todos los atributos
Crea una instancia de Estudiante y prueba el método to_dict()
Comprueba que el diccionario contiene toda la información del objeto
'''
class Estudiante:
    def __init__(self, nombre: str, edad: int,calificaciones: list) -> None:
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones
    
    def to_dict(self) -> dict:
        return {'nombre': self.nombre,
                'edad': self.edad,
                'calificaciones': self.calificaciones}

alumno = Estudiante('Josias', 3, [10,10,10,10])

print(alumno.to_dict())