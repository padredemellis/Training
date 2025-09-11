"""
¿ES UN ANAGRAMA? 
Escribe una función que reciba dos palabras (String) y retorne 
verdadero o falso (Bool) según sean o no anagramas. 
Un Anagrama consiste en formar una palabra reordenando TODAS 
las letras de otra palabra inicial. 
NO hace falta comprobar que ambas palabras existan. 
Dos palabras exactamente iguales no son anagrama. 
"""
def anagram (str1, str2):
    if len(str2) != len(str1) or str1 == str2:
        return False
    
    if sorted(str1.lower()) == sorted(str2.lower()) and str1 != str2:
        return True
    else:
        return False
    
cadena1 = "Sergio"
cadena2 = "riesgO"

print(anagram(cadena1, cadena2))