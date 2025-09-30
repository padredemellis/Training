from random import randint
def guessTheNumber(name, numberUser):
    print(f"{name} You must guess a number from 1 to 100")
    numberNPC = randint(0, 101)
    counter = 0
    for i in range(9):
        if (numberUser < 1) or (numberUser > 100):
            return (f"The number: {numberUser} is not allowed")  
        elif numberUser < numberNPC:
            return(f"The user's number {numberUser} is less than the NPC's number.")
        elif numberUser > numberNPC:
            return(f"The user's number {numberUser} is greater than the NPC's number.")
        else:
            print(f"You'are de champion the number win it's {numberNPC}")
            print(f"you did it in {counter} attempts")
            return
        counter += 1

test = guessTheNumber(input("Enter your name: "), int(input("enter an number: ")))

print(test)
            