"""
You will need to create a program in Python that continues until the user exits the program.

The user should be able to choose from a number of options, and each should cause the program to execute a different task. (Note: the final option should exit the program).

These tasks can be whatever you like; printing something to the terminal, making calculations, retrieving input from the user - the choice is yours!

"""

#spell words: 
#random numbers
#random words: say, whisper, shout 
#random actions: wave, flick
#ask user what the spell is for
#build random spell from lists
#print spell 
#if else to ask if they want to continue

import random
#Create global variables
Number = 0
def GenerateSpells():
    Importantance = str(input("Is the spell you are casting today either: 1. Crucial  2. Important 3. Just for fun \nType in your response: "))
    if Importantance == "1" or Importantance == "Crucial":
        Number = random.randrange(20, 50)
    elif Importantance == "2" or Importantance== "Important":
        Number = random.randrange(10, 20)
    elif Importantance == "3" or Importantance == "Just for fun":
            Number = random.randrange(2, 10)
    else:
        print("\n<<~~***~~>>\nCasting a spell didn't work, please type in why you want to cast a spell again:")
        GenerateSpells()
    #Random words
    wordList = ["say", "shout", "whisper", "declare", "chant"]
    randomWord = random.choice(wordList)
    #Random spells
    spellList = ["ACCIO", "LUMOS", "OCULUS REPARO", "Petrificus Totalus", "Expectro Patrono", "Wingardium Leviosa"]
    randomSpell = random.choice(spellList)
    randomSpell = randomSpell.title()
    #Random actions
    actionList = ["Wave", "Flick", "Circle"]
    randomAction = random.choice(actionList)
    
    spell = print(f"\n<<~~***~~>>\nTo cast a spell you must follow these directions: \n{randomAction} your wand {Number} times and {randomWord} {randomSpell}.")
    Continue = str(input("Do you need to generate more spells? \n Type in yes or no: "))
    if Continue == "Yes" or Continue == "yes" or Continue == "y":
         GenerateSpells()
    else:
        print("I hope the spell works!")
    return spell

GenerateSpells()
