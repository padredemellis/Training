#Ejercicio 1: Convierte un texto a minúsculas
texto = "Hola MUNDO"
print(texto.lower())
#Ejercicio 2: Cuenta cuántas veces aparece una letra en un texto
texto = "programacion"
letra = "a"
print(texto.count(letra))
#Ejercicio 3: Obtén la primera y última letra de un texto
texto = "Python"
print(f"{texto[0]} - {texto[-1]}")
#Ejercicio 4: Convierte un string en una lista de palabras
texto = "Hola mundo desde Python"
texto = texto.split()
print(f"{type(texto)} {texto}")
#Ejercicio 5: Une una lista de palabras en un string
palabras = ["Python", "es", "genial"]
cadena = (" ").join(palabras)
print(cadena)
#Ejercicio 6: Cuenta elementos en una lista
frutas = ["manzana", "banana", "cereza", "manzana"]
print(len(frutas))
#Ejercicio 7: Invierte el orden de una lista
numeros = [1, 2, 3, 4, 5]
print(numeros[::-1])
#Ejercicio 8: Crea una lista con 3 letras elegidas por el usuario
lista = []
for l in range(3):
    lista.append(input("ingresa una letra\n").lower())
print(lista)
#Ejercicio 9: Recorre una lista y procesa cada elemento
letras = ['a', 'e', 'i']
texto = "programacion"
for l in letras:
    if l in texto:
        print(f'{l} Se encuentra {texto.count(l)} veces')
    else:
        print(f'{l} no se encuentra en {texto}')
#Ejercicio 10: Verifica si un elemento existe en una lista
palabras = ["python", "java", "javascript"]
buscar = "python"
buscador = buscar in palabras
existe = {
    True: f"Sí! {buscar} esta en {palabras}",
    False: f"No! {buscar} no esta en {palabras}"
}
print(existe[buscador])
#Ejercicio 11: Pide texto al usuario y muestra su longitud
texto = input("Ingresa un texto\n")
print(f"Su longitud es: {len(texto)}")
#Ejercicio 12: Pide 3 letras al usuario y guárdalas en una lista
lista = []
for l in range(3):
    lista.append(input("ingresa una letra: "))
print(lista)
#Ejercicio 13: Cuenta palabras en un texto ingresado por el usuario
texto = input("Ingresa un texto\n")
textoALista = texto.split(" ")
print(f"el texto dice {textoALista}")
print(f"Su longitud es: {len(textoALista)}")
#Ejercicio 14: Busca si existe una palabra específica en un texto
texto = "hola bro"
buscar = "Napoleon" in texto
print(f"Mas {buscar} que las promesas de tu eX")
#Ejercicio 15: Muestra el texto con palabras en orden inverso
texto = "hola bro"
invertir = texto.split()
print(f" {" ".join(invertir[::-1])} ")
#Ejercicio 16: Usa un diccionario para respuestas True/False
respuestas = {True: "Sí se encuentra", False: "No se encuentra"}
texto = "Jesus" in "Jesus lloró"
print(respuestas[texto])
#Ejercicio 17: Combina conteo de múltiples letras
texto = "Este es un texto de prueba"
letras = ['e', 's', 't']
for l in letras:
    if l in texto:
        print(f"{l} se encuentra {texto.count(l)} veces")
#Ejercicio 18: Función que analiza primera y última letra
def analizar_extremos(texto):
    return f"La primera letra es {texto[0]} y la ultima es {texto[-1]}"

print(analizar_extremos("Hola bro"))
#Ejercicio 19: Función que invierte palabras de un texto
def invertir_palabras(texto):
    return f"{" ".join(texto[::-1])}"

print(invertir_palabras("Hola bro"))