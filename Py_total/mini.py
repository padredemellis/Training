
print("\n📝 STRINGS Y MÉTODOS (Ejercicios 1-20)\n")
print("**Básicos:**\n")
print("\n1. Crear una variable con tu nombre y mostrar su longitud")
name = "Emanuel"
print(f"Your name is {name} and its size is {len(name)}")
print("End of the exercise".center(50,"*"))
print('\n2. Convertir la frase "Hola Mundo" a minúsculas')
print("Hola Mundo".lower())
print("End of the exercise".center(50,"*"))
print('\n3. Convertir "python programming" a mayúsculas')
print("python programming".upper())
print("End of the exercise".center(50,"*"))
print("\n4. Contar cuántas veces aparece la letra 'a' en 'programación'")
text = "programación"
print(text.count("a"))
print("End of the exercise".center(50,"*"))
print("\n5. Reemplazar todas las 'o' por '0' en 'Hello World'")
text = 'Hello World'
print(text.replace("o","0"))
print("End of the exercise".center(50,"*"))
print("\n**Intermedios:**\n")
print('\n6. Verificar si la palabra "Python" está en "Me gusta Python programming"')
text = "Me gusta Python programming"
word = "Python" in text
bool = {True: "Yes! The word is found", False: "No! The word is not found."}
print(bool[word])
print("End of the exercise".center(50,"*"))
print("\n7. Encontrar la posición de la primera 'e' en 'desarrollador'")
text = 'desarrollador'
print(f"The position of the first 'e' is {text.index("e")}")
print("End of the exercise".center(50,"*"))
print('\n8. Dividir la frase "uno,dos,tres,cuatro" usando la coma como separador')
phrase = "uno,dos,tres,cuatro"
print(phrase.split(","))
print("End of the exercise".center(50,"*"))
print("\n9. Unir la lista ['Python', 'es', 'genial'] con espacios")
listOfWords = ['Python', 'es', 'genial']
string = " ".join(listOfWords)
print(string)
print("End of the exercise".center(50,"*"))
print('\n10. Eliminar espacios al inicio y final de "  Hola Python  "')
text = "  Hola Python  "
print(text.strip())
print("End of the exercise".center(50,"*"))
print("\n**Avanzados:**\n")
def countingVowels(text):
    text = text.lower()
    vowels = []
    counter = 0
    if "a" in text:
        vowels.append("a")
    if "e" in text:
        vowels.append("e")
    if "i" in text:
        vowels.append("i")
    if "o" in text:
        vowels.append("o")
    if "u" in text:
        vowels.append("u")
        
    for vowel in vowels:
        counter = text.count(vowel)
        print(f"The vowel {vowel} appears {counter} times")
    return "Exit"
test = countingVowels("Murciélago es un insecto que tiene fuertes caninos y los molares con puntas cónicas. Tiene formado el dedo índice de las extremidades torácicas por solo una o a lo más dos falanges y sin uña. ")
print(test)
print("End of the exercise".center(50,"*"))

print("\n12. Hacer un programa que determine si una palabra es palíndromo")
def palindrome(word):
    if word.lower() == word[::-1].lower():
        return f"{word} is Palindrome"
test = palindrome("Reconocer")
print(test)
print("End of the exercise".center(50,"*"))

print('\n13. Capitalizar solo la primera letra de cada palabra en "hola mundo python"')
def capitalice(text):
    dividir_text = text.split(" ")
    newPrhase = " "
    textList = []
    word = " "
    for t in dividir_text:
        word = t
        word = word.capitalize()
        textList.append(word)
    newPrhase = " ".join(textList)
    print(newPrhase)
    
capitalice("hola mundo python")
print("End of the exercise".center(50,"*"))
    
print('\n14. Extraer solo los números de "abc123def456"')
number = []
def cutNumbers(text):
    for t in text:
        if t.isdecimal():
            number.append(t)
    return f"{number}"
print(cutNumbers("abc123def456"))
print("End of the exercise".center(50,"*"))

print("\n15. Verificar si un string contiene solo letras")
string = "soloLetras3"
if string.isalpha():
    print(f"{string} is True")
else:
    print(f"{string} is False")
print("End of the exercise".center(50,"*"))

print("\n16. Crear un función que invierta solo las letras de un string")
def invertWords(text):
    listWord = []
    for t in text:
        if t.isalpha():
            listWord.append(t)
    wordsLetters = "".join(listWord)
    wordsLetters = wordsLetters[::-1]
    return(wordsLetters)
print(invertWords("123Hello"))        
print("End of the exercise".center(50,"*"))

print("\n17. Contar palabras en un párrafo (sin usar split())")

def countingWords_v2(text):
    text = text.strip() 
    if not text:
        return 0 
    
    word_count = 0
    is_word = False 
    
    for char in text:
        if char.isalpha():
            if not is_word:
                word_count += 1
                is_word = True
        else:
            is_word = False
            
    return word_count

print(f"El texto es: 'Hola bro'")
print(f"Número de palabras: {countingWords_v2('Hola bro')}")

print(f"El texto es: '  Uno dos tres   '")
print(f"Número de palabras: {countingWords_v2('  Uno dos tres   ')}")

print(f"El texto es: 'Uno-dos,tres'")
print(f"Número de palabras: {countingWords_v2('Uno-dos,tres')}")
print("End of the exercise".center(50,"*"))

print("\n18. Encontrar la palabra más larga en una frase")
def phraseLength(text):
        text = text.split(" ")
        bigWord = max(text, key=len)
        return bigWord
print(phraseLength("¿ Cuál será la palabra mas larga de estas ?"))
    
print("End of the exercise".center(50,"*"))

print("\n19. Reemplazar múltiples espacios por uno solo")
def replaceSpace(text):
    text = text.split()
    union = " ".join(text)
    return union
print(replaceSpace("Hola     , Mundo"))
print("End of the exercise".center(50,"*"))

print("\n20. Crear un validador de email básico")

def validateEmail(email):
    valido = "@gmail.com"
    if valido in email:
        return True
    else:
        return False
print(validateEmail("gandalfForEver@gmail.com"))
#Pendiente...hacerlo con el modulo RE
print("End of the exercise".center(50,"*"))

print("\n## 📋 LISTAS Y INDEXACIÓN (Ejercicios 21-35)")

print("**Básicos:**\n")
print("\n21. Crear una lista con 5 frutas y mostrar la primera y última")
listFruits = ["Apple", "Banana", "Orange", "Cherry", "Lemon"]
print(listFruits[0], listFruits[-1])

print("\n22. Agregar un elemento al final de una lista")
listFruits.append("Kiwi")
print(listFruits)
print("End of the exercise".center(50,"*"))

print("\n23. Insertar un elemento en la posición 2 de una lista")
def insertElement(listElement: list):
    listElement.insert(2,input("insert an element: "))
    return listElement
listElement = [1,2,3,4]
print(insertElement(listElement))
print("End of the exercise".center(50,"*"))

print("\n24. Eliminar el último elemento de una lista")
def deleteElement(listElement: list):
    listElement.pop()
    return listElement
listElement = [1,2,3,4]
print(deleteElement(listElement))
print("End of the exercise".center(50,"*"))

print("\n25. Encontrar el índice de un elemento específico")
def findElement(listElement,element):
    if element in listElement:
        return listElement.index(element)
listElement = [input("enter an element: ") for e in range(6)]
element = input("enter an element to find: ")
print(findElement(listElement, element))
print("End of the exercise".center(50,"*"))

print("**Intermedios:**")
print("26. Invertir una lista sin usar reverse()")
def reverseList(listToReverse):
    return listToReverse[::-1]
listToReverse = [input("enter an element") for e in range(3)]
print(reverseList(listToReverse))
print("End of the exercise".center(50,"*"))

print("27. Encontrar el elemento mayor y menor de una lista numérica")
def findMaxMin(listTofind):
    elementMax = max(listTofind)
    elementMin = min(listTofind)
    return f"Max = {elementMax} & Min = {elementMin}"
print(findMaxMin([2,4,8,9,10,0]))
print("End of the exercise".center(50,"*"))

print("28. Crear una nueva lista con solo elementos únicos")
unique_elements = list({1,2,1,2,3,4,5})
print(unique_elements)
print("End of the exercise".center(50,"*"))

print("29. Combinar dos listas alternando elementos")
listOne = [1,2,3,4]
listTwo = ["a","b","c","d"]
unitedList = list(zip(listOne, listTwo))
for n, l in unitedList:
    print(f'Letra: {l}, y Número: {n}')
print("End of the exercise".center(50,"*"))
print("End of the exercise".center(50,"*"))
print("30. Dividir una lista en dos mitades")
def twoHalves(listTocut: list):
    listOne = []
    listTwo = []
    lenght = len(listTocut)
    if lenght % 2 == 0:
        listOne = listTocut[0:lenght //2]
        listTwo = listTocut[lenght //2:]
    else:
        listOne = listTocut[0: lenght //2 + 1]
        listTwo = listTocut[lenght // 2 + 1:]
    return f"La primer mitad es: {listOne}\nLa segunda mitad es: {listTwo}"
print(twoHalves([1,2,3,4]))
"""
**Avanzados:**
31. Crear una función que ordene una lista sin usar sort()
32. Encontrar elementos comunes entre dos listas
33. Rotar elementos de una lista hacia la derecha
34. Crear sublistas de tamaño n de una lista grande
35. Implementar búsqueda binaria en una lista ordenada

## 🎯 TUPLAS Y ESTRUCTURAS DE DATOS (Ejercicios 36-45)

36. Crear una tupla con coordenadas (x, y) y acceder a cada valor
37. Convertir una lista a tupla y viceversa
38. Crear un diccionario con datos personales
39. Agregar y eliminar elementos de un diccionario
40. Iterar sobre las claves y valores de un diccionario
41. Crear una lista de tuplas con nombre y edad
42. Usar tuplas como claves de diccionario
43. Crear un conjunto (set) y realizar operaciones básicas
44. Encontrar intersección entre dos conjuntos
45. Crear una estructura de datos anidada (lista de diccionarios)

## 🔢 ENTRADA DE USUARIO Y CONVERSIONES (Ejercicios 46-55)

46. Pedir nombre al usuario y saludarlo personalizado
47. Solicitar un número y verificar si es par o impar
48. Pedir dos números y mostrar todas las operaciones matemáticas
49. Validar que la entrada del usuario sea un número válido
50. Crear un menú simple con opciones numeradas
51. Pedir una lista de números separados por comas
52. Convertir temperatura de Celsius a Fahrenheit
53. Calcular el área de diferentes figuras geométricas
54. Crear una calculadora básica con menú
55. Validar entrada de contraseña con criterios específicos

## 🎮 CONTROL DE FLUJO Y LÓGICA (Ejercicios 56-70)

**Condicionales:**
56. Determinar si un año es bisiesto
57. Clasificar edad en categorías (niño, adolescente, adulto)
58. Crear un sistema de calificaciones (A, B, C, D, F)
59. Verificar si un triángulo es válido dados tres lados
60. Determinar el mayor de tres números

**Bucles:**
61. Imprimir números del 1 al 100 que sean múltiplos de 3
62. Crear una tabla de multiplicar para cualquier número
63. Sumar todos los números pares del 1 al 1000
64. Encontrar todos los números primos menores a 100
65. Crear un patrón de asteriscos (triángulo)

**Combinados:**
66. Juego de piedra, papel o tijera
67. Generador de contraseñas aleatorias
68. Contador de intentos con límite máximo
69. Validador de rango numérico con reintentos
70. Sistema de autenticación simple

## 🎯 PROYECTOS INTEGRADOS (Ejercicios 71-80)

**Analizador de Texto (preparación):**
71. Crear función que cuente letras específicas en un texto
72. Función que convierta texto completo a minúsculas
73. Contador de palabras en cualquier texto
74. Función que extraiga primera y última letra
75. Invertir orden de palabras en una frase

**Juego de Adivinanza (preparación):**
76. Generar número aleatorio en rango específico
77. Validar que entrada esté en rango permitido
78. Contador de intentos con límite
79. Sistema de pistas (mayor/menor)
80. Función que determine victoria o derrota
"""