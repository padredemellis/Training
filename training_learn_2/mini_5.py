'''
Ejercicio 5: Inicialización de Equipos
Escribe una función que tome un nombre de equipo y cree un nuevo registro con todas las estadísticas inicializadas a cero.
'''
from mini_4 import diccionario

def name_team(team_name: str) -> dict:
    diccionario = {'team': team_name, "games played": 0, "win": 0, "draw": 0, "loss": 0, "points": 0 }
    return diccionario

new_team = name_team('Peñarol')

print(new_team)
