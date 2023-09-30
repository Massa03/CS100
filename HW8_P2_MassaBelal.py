#Massa Belal
#CS 100 2021F Section 035
#HW 08, October 25, 2021

#2
import string

def twoWords(integer, character):
    wordList = []
    userInput = ''
    userInput2 = ''
    while len(userInput) != integer:
        userInput = input("Enter a " + str(integer) + "-letter word please:")
        wordList.append(userInput)
    while userInput2 != character:
        userInput2 = input("Enter a word beginning with " + character + " please:")
        if userInput2[0] == character:
            wordList.append(userInput2)
            return(wordList)
       
print(twoWords(4, 'B'))
