'''
You're going to create a program that first asks the user to enter text. It can be any text: an entire article, a paragraph, a sentence, a poem, whatever. Then, the program will ask the user to also enter three letters of their choice, and from that point on, our code will process that information to perform five types of analysis and return the following information to the user: 1. First: How many times does each of the letters they chose appear? To accomplish this, I recommend storing those letters in a list and then using a string-specific method that allows us to count how many times a substring appears within the string. Something you should keep in mind is that when searching for letters, there may be uppercase and lowercase letters, and this will affect the result. To ensure that absolutely all letters are found, you should convert both the original text and the letters you want to search for to lowercase. 2. Second: You'll tell the user how many words there are in the entire text.
And to accomplish this, remember that there's a string method that allows you to transform it into a list, and then there's a function that allows you to find out the length of a list.
3. Third: It will tell us what the first letter of the text is and what the last. Here, we'll clearly use indexing.
4. Fourth: The system will show us how the text would look if we reversed the order of the words. Is there a method that allows you to reverse the order of a list, and another that allows you to join those elements with spaces in between? Think about it.
5. And finally: The system will tell us if the word "Python" is found in the text. This part might be a bit tricky to figure out, but I'll give you a hint:
you can use Booleans to do your research and a dictionary to find a way to express your answer to the user.
'''
text = input("Ingresa el texto: ").lower()
letters = []
for i in range(3):
    letter = input(f"Ingresa la letra {i+1}: ").lower()
    letters.append(letter)

print("=== ANÁLISIS DE LETRAS ===")
for letter in letters:
    count = text.count(letter)
    print(f"La letra '{letter}' aparece {count} veces")

words_list = text.split()
word_count = len(words_list)
print(f"\n=== CONTEO DE PALABRAS ===")
print(f"El texto tiene {word_count} palabras")

print(f"\n=== PRIMERA Y ÚLTIMA LETRA ===")
print(f"Primera letra: '{text[0]}'")
print(f"Última letra: '{text[-1]}'")

words_list.reverse()
reversed_text = " ".join(words_list)
print(f"\n=== TEXTO CON PALABRAS INVERTIDAS ===")
print(f"Texto invertido: {reversed_text}")

print(f"\n=== BÚSQUEDA DE 'PYTHON' ===")
python_found = "python" in text
result_dict = {True: "Sí se encontró", False: "No se encontró"}
print(f"¿Se encontró 'python'? {result_dict[python_found]}")
'''
def counter(phrase: str, letterA: str, letterB: str, letterC: str):
    countA = 0
    countB = 0
    countC = 0
    
    
    if letterA in phrase:
        countA = phrase.count(letterA)
    if letterB in phrase:
        countB = phrase.count(letterB)
    if letterC in phrase:
        countC = phrase.count(letterC)
    
    print(f"This letter {letterA} appears {countA}\nThis letter {letterB} appears {countB}\n This letter {letterC} appears {countC}")
    print(f"This first letter it's:'{phrase[0]}' and the last it's: '{phrase[-1]}'")
    transform = phrase.split(" ")
    print(f"The lengh of '{phrase}' it's: {len(transform)}")
    print(f"The invert of '{phrase}' it's: {phrase[::-1]}")
    appears = "python" in phrase
    print(f"python appers in {phrase}:{appears}")
    
enter_text = counter(input("enter an phrase\n").lower(),
                     input("enter first letter\n").lower(),
                     input("enter second letter\n").lower(),
                     input("enter third letter\n").lower())
print(enter_text)
'''
