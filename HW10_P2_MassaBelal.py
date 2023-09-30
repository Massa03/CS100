# Massa Belal
# CS 100 2021F Section 035
# HW 10, November 8,2021

#2

def initialLetters(wordList):
	d = {}
	for word in wordList:
		# word = 'say'
		iLetter = word[0]
		# iLetter = 's'
		if iLetter in d:
			if word not in d[iLetter]:
				print(f"{word} not in dict, so adding")
				d[iLetter].append(word)
			else:
				print(f"{word} already FOUND in dict")
		else:
			print(f"No letters beggining with {iLetter}, adding key with value {[word]}")
			d[iLetter] = [word]
	return d
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say', 'said'] 

print(initialLetters(horton))
