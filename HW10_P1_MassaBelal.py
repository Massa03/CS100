# Massa Belal
# CS 100 2021F Section 035
# HW 10, November 8,2021

#1

def initialLetterCount(wordList):
	d = {}
	for word in wordList:
		if word[0] in d:
			# word = 'say'
			d[word[0]] = d[word[0]] + 1
		else:
			d[word[0]] = 1
	return d
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say'] 
print(initialLetterCount(horton))
