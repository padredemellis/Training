'''
Objetivo: Integrar conceptos de clases, serialización y argumentos.

Instrucciones:

Crea una clase básica Vehiculo con atributos marca y modelo
Añade dos subclases: Coche (con atributo puertas) y Moto (con atributo cilindrada)
Implementa métodos para serializar a JSON y cargar desde JSON
Crea un sistema de línea de comandos simple que permita:
Crear un vehículo (coche o moto) y guardarlo
Cargar un vehículo por marca y modelo
'''
import json
import sys

class Vehiculo:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo
    
    def to_dict(self) -> dict:
        # Método base que las subclases ampliarán
        return {
            'tipo': self.__class__.__name__,  # Guarda el tipo de la clase
            'marca': self.marca,
            'modelo': self.modelo
        }
    
    def __str__(self) -> str:
        return f"{self.marca} {self.modelo}"
    
    def guardar_json(self) -> str:
        # Genera nombre de archivo a partir de marca y modelo
        archivo = f"{self.marca}_{self.modelo}.json".replace(" ", "_")
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=4)
        return archivo
    
    @classmethod
    def cargar_json(cls, archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            
            # Determina qué tipo de vehículo crear
            tipo = datos.get('tipo', '')
            if tipo == 'Coche':
                return Coche(marca=datos['marca'],
                            modelo=datos['modelo'],
                            puertas=datos['puertas'])
            elif tipo == 'Moto':
                return Moto(marca=datos['marca'],
                          modelo=datos['modelo'],
                          cilindrada=datos['cilindrada'])
            else:
                raise ValueError(f"Tipo de vehículo desconocido: {tipo}")

class Coche(Vehiculo):
    def __init__(self, marca: str, modelo: str, puertas: int) -> None:
        super().__init__(marca, modelo)
        self.puertas = puertas
    
    def to_dict(self) -> dict:
        datos = super().to_dict()
        datos['puertas'] = self.puertas
        return datos
    
    def __str__(self) -> str:
        return f"{super().__str__()} - Puertas: {self.puertas}"

class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, cilindrada: float) -> None:
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    
    def to_dict(self) -> dict:
        datos = super().to_dict()
        datos['cilindrada'] = self.cilindrada
        return datos
    
    def __str__(self) -> str:
        return f"{super().__str__()} - Cilindrada: {self.cilindrada}cc"

def main():
    # Verificar que hay suficientes argumentos
    if len(sys.argv) < 2:
        print("Uso: python script.py <crear|cargar> [argumentos]")
        sys.exit(1)
    
    comando = sys.argv[1].lower()
    
    if comando == "crear":
        # Verificar argumentos para crear
        if len(sys.argv) < 5:
            print("Para crear: python script.py crear <tipo> <marca> <modelo> <puertas|cilindrada>")
            sys.exit(1)
        
        tipo = sys.argv[2].lower()
        marca = sys.argv[3]
        modelo = sys.argv[4]
        valor = sys.argv[5]  # puertas o cilindrada
        
        # Crear el vehículo según su tipo
        if tipo == "coche":
            vehiculo = Coche(marca, modelo, int(valor))
        elif tipo == "moto":
            vehiculo = Moto(marca, modelo, float(valor))
        else:
            print(f"Tipo de vehículo no reconocido: {tipo}")
            sys.exit(1)
        
        # Guardar y mostrar información
        archivo = vehiculo.guardar_json()
        print(f"Vehículo guardado: {vehiculo}")
        print(f"Archivo: {archivo}")
        
    elif comando == "cargar":
        # Verificar argumentos para cargar
        if len(sys.argv) < 4:
            print("Para cargar: python script.py cargar <marca> <modelo>")
            sys.exit(1)
        
        marca = sys.argv[2]
        modelo = sys.argv[3]
        
        # Generar nombre de archivo
        archivo = f"{marca}_{modelo}.json".replace(" ", "_")
        
        try:
            # Cargar vehículo
            vehiculo = Vehiculo.cargar_json(archivo)
            print(f"Vehículo cargado: {vehiculo}")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo}")
            sys.exit(1)
    else:
        print(f"Comando desconocido: {comando}")
        print("Uso: python script.py <crear|cargar> [argumentos]")
        sys.exit(1)

if __name__ == "__main__":
    main()