'''
Ejercicio 3: Formateo Básico
Crea una función que tome un nombre de equipo y lo formatee para que ocupe exactamente 30 caracteres, rellenando con espacios a la derecha.
'''
def name_team(team_name: str) -> str:
    return team_name.ljust(30-len(team_name)," ")

team = 'Peñarol'

print(name_team(team))

'''
A considerar ,el primer parametro de ljust marca los caracteres maximos incluyendo las palabras que le pase como argumento
'''