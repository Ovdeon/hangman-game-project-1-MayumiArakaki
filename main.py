import json
import random

with open("words.json") as data:
    list = json.load(data)
# print(list["data"])

def randomWord ():
    aleatorio = random.choice(list["data"])
    return aleatorio

def printWord(word,letterChoisen):
    l = len(word)
    letters = []
    for i in range(l):
        if word[i] in letterChoisen:
            letters.append(word[i])
        else:
            letters.append("_")
    return letters

def WinCondition(word):
    if "_" in word:
        return False
    return True

def drawHangman(array,error):
    print(array[error])    

hangMan = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

chosenWord = str(randomWord())
print(chosenWord)
errors = 0
chosenLetter = []
a = printWord(chosenWord,chosenLetter)
print(a)

while errors <= 5:
    x = input("Ingrese la letra: ")
    if not(x.isnumeric) or not(x.isalpha) or (x in chosenLetter) or not(x in chosenWord):
        chosenLetter.append(x)
        errors = errors + 1
        print("Haz perdido una oportunidad, te quedan " + str(6-errors))
        drawHangman(hangMan,errors)
        if errors == 6:
            print("Haz perdido")
    elif x in chosenWord:
        chosenLetter.append(x)
        if WinCondition(printWord(chosenWord,chosenLetter)):
            print(printWord(chosenWord,chosenLetter))
            print("Felicidades Has ganado")
            break
        print(printWord(chosenWord,chosenLetter))
