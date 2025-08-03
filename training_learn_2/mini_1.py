'''
Ejercicio 1: Separación de Datos
Escribe una función que reciba una cadena como "Equipo1;Equipo2;resultado" y devuelva una lista con los tres elementos separados.
'''
def data_separation(cadena: str) -> list:
    return cadena.split(';')

cadena = 'Equipo1;Equipo2;resultado'

print(data_separation(cadena))

'''Observaciones'''
'''
El metodo split sirve para separar una string y convertirla en una lista
'''