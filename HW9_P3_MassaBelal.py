#Massa Belal
#CS 100 2021F Section 035
#HW 09, November 3, 2021

#2

import string 

def repeat_words(in_file, out_file):
    inF = open(in_file)
    outF = open(out_file,'w')
    text = inF.read()
    words = text.split()
    counts = 0
    wordLst = []
    for word in words:
        wordLst.append(words)
    for word in in_file:
        newWord = word.lower() or word.upper()
        if newWord in wordLst:
            counts += wordLst.count(newWord)
            outF.write(inF.read())
            inF.close()
            outF.close()
            
repeat_words('catInTheHat.txt', 'catRepWords.txt')
