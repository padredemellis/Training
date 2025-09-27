myTxt = "This is a test"
"""Displays the contents of the index"""
print(myTxt[0]) #T
print(myTxt[-1])#t
'''find the first occurrence of the letter from left to right'''
print(myTxt.index("a")) #8
print(myTxt.index("t", 5, 14))# 10 
'''from right to left'''
print(myTxt.rindex("t"))# 13
#print(myTxt.index("A")) #ValueError

'''Slicing'''
myTxt = "This is a test"
print(myTxt[0:4]) #This
email = 'emanuelromero@gmail.com'
print(email[13:]) #"@gmail.com"
print(email[:13])#"emanuelromero"
print(email[::3])# skips every three characters
print(email[::-1])#"moc.liamg@oremorleuname" -> invert strings

name = "Jesus"
print(name.upper()) #JESUS
print(name.lower()) #jesus
print(name.split()) #[J,e,s,u,s] -> transforms a string into a list
print(name.split("s")) #["Je","u",""]
print(name.find("sus")) #2
print(name.replace("u", "ú" )) #Jesús

learn = "learn"
python = "python"
space = " ".join([learn,python])
print(type(space))
print(space) #learn python


print("is good" in space) #False
print("py" not in space) #False

print(len(space)) #12 calcultes the length of string
