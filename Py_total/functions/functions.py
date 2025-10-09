def my_function(name):
    """This function displays a greeting on the screen."""
    return f"Hello {name}"

print(my_function("Mayra"))

def add(num1, num2):
    return num1 + num2

result = add(32, 45)
print(f"This result is: {result}")

def threeDigits(number):
    return abs(number) in range(100,1000)

result = threeDigits(-555)
print(result)

def desempacarTuples(tuple: tuple) -> list:
    newTuple = []
    for name, lastName in tuple:
        newTuple.append(name)
    return newTuple
print(desempacarTuples(((input("name: "), input("lastname: ")),(input("name: "), input("lastname: ")))))
from random import shuffle
firstList: list = ["-","--","---","----"]


def mezclarPalitos(newList):
    shuffle(newList)
    return newList


def intentoUser():
    intento = " "
    while intento not in ["1","2","3","4"]:
        intento = input("elige un numero del 1 al 4: ")
    return int(intento)

def numeroGanador(lista, intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    print(f"Te ha tocado {lista[intento - 1]}")

palitosMezclados = mezclarPalitos(firstList)
seleccion = intentoUser()
numeroGanador(palitosMezclados, seleccion)