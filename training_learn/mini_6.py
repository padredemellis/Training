'''
Objetivo: Practicar la serialización de objetos a JSON y viceversa.

Instrucciones:

Importa el módulo json
Crea una clase Contacto con atributos nombre, email y telefono
Añade un método guardar_json(archivo) que guarde el objeto como JSON en un archivo
Añade un método de clase cargar_json(archivo) que cargue un contacto desde un archivo
Prueba guardando un contacto y luego cargándolo
'''
import json

class Contacto:
    def __init__(self, nombre: str, email: str, telefono: str) -> None:
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    def to_dict(self) -> dict:
        return {'nombre': self.nombre,
                'email': self.email,
                'telefono': self.telefono}
    
    
    def guardar_json(self, archivo) -> None:
        contacto_dict = self.to_dict()
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(contacto_dict, f, indent= 4)
    
    @classmethod
    def cargar_json (cls,archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            contacto_dict = json.load(f)
            
            return cls(nombre = contacto_dict['nombre'],
                   email = contacto_dict['email'],
                   telefono = contacto_dict['telefono'])

persona = Contacto('Mayra', 'mayra@dachi.como', '093373773')
datos = 'datos.json'
persona.guardar_json(datos)
persona.cargar_json(datos)