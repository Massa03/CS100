# Massa Belal
# CS 100 2021F Section 035
# HW 10, November 8,2021

#3

def shareOneLetter(wordList):
	d = {}
	# initialize the dict
	for word in wordList:
		d[word] = []
#----------------------------
	for key in d.keys():
		# go through all words
		for word in wordList:
			# go through letters of words
			for char in word:
				# add char if incuded
				if char in key:
					# add IF NOT ALREADY IN LIST
					if word not in d[key]:
						d[key].append(word)
	return d
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say'] 
print(shareOneLetter(horton))