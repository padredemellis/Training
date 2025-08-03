'''
Ejercicio 2: Procesamiento Condicional
Escribe una función que tome un resultado ("win", "loss" o "draw")
y devuelva los puntos correspondientes para el primer equipo (3 para victoria, 1 para empate, 0 para derrota).
'''
def result(resultado: str) -> int:
    puntos = {'win': 3, 'loss': 0, 'draw': 1}
    if resultado in puntos:
        return puntos[resultado]
    else:
        raise ValueError('Debes escribir [win] - [loss] - [draw]')

resultado = input("ingrese un resultado: (win, loss, draw)\n").lower()

puntaje = result(resultado)

print(puntaje)

'''
Fijarse si puedo simplificar una estructura condicional en un diccionario
No olvidarse del raise ValueError en estos casos de multiples condiciones
'''