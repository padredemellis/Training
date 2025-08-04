'''
Ejercicio 4.2: Acceso a Valores
Escribe una función que reciba un diccionario con información de un equipo
y devuelva una cadena con el formato: "El equipo [nombre] de [país] tiene [número] jugadores."
'''
def info_team(team: dict) -> str:
    info_team = {'name': '',
                 'Country': '',
                 'number': 0}
    return f"Team {info_team['name']} from {info_team['Country']} has {info_team['number']} players."