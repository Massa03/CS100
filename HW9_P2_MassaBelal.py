#Massa Belal
#CS 100 2021F Section 035
#HW 09, November 3, 2021

#2

def file_stats(in_file):
    inF = open(in_file)
    text = inF.read()
    char = len(text)
    lines = text.count('\n')
    words = len(text.split())
    print('lines',lines)
    print('words', words)
    print('characters', char)

    inF = close(in_file)
    
file_stats('created_equal.txt') 
    
    
    
