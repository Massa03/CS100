#Massa Belal
#CS 100 2021F Section 035
#HW 08, October 25, 2021

#1
import string 
integer = 6

def twoWords(integer, character):
    wordList = []
    while True:
        userInput = input("Enter a " + str(integer) + "-letter word please:")
        if len(userInput) == integer:
            wordList.append(userInput)
            break
    while True:
        userInput = input("Enter a word beginning " + character + " please:")
        if userInput[0] == character.upper() or  userInput[0] == character.lower():
            wordList.append(userInput)
            break
    return(wordList)
       
print(twoWords(6, 'A'))
