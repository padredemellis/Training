'''
Ejercicio 6: Colección de Equipos
Implementa una función que mantenga un diccionario de todos los equipos, añadiendo nuevos equipos cuando sea necesario.
'''
def add_team_if_not_exists(teams_dict: dict, team_name: str) -> dict:
    if team_name not in teams_dict:
        teams_dict[team_name] = {
            "nombre": team_name,
            "partidos_jugados": 0,
            "victorias": 0,
            "empates": 0,
            "derrotas": 0,
            "puntos": 0
        }
    
    return teams_dict

# Ejemplo de uso:
all_teams = {}  # Diccionario vacío inicialmente
all_teams = add_team_if_not_exists(all_teams, "Peñarol")
all_teams = add_team_if_not_exists(all_teams, "Nacional")
all_teams = add_team_if_not_exists(all_teams, "Peñarol")  # No debería añadirse de nuevo

print(all_teams)  # Debería mostrar solo dos equipos (Peñarol y Nacional)