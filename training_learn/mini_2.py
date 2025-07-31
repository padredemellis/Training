'''
📝 Mini-Ejercicio 2: Método __str__
Objetivo: Entender cómo hacer que los objetos sean imprimibles directamente.

Instrucciones:

Crea una clase Producto con atributos nombre y precio
Implementa el método __str__ para que al imprimir un producto se muestre: "Producto: [nombre] - $[precio]"
Crea varios productos e imprímelos directamente
'''
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self) -> str:
        return f'Producto: [{self.nombre}] - $[{self.precio}]'

if __name__ == '__main__':
    nintendo = Producto('Nintendo Swich 2', 700)
    print(nintendo)