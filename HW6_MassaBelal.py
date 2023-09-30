# Massa Belal
#CS 100 2021F Section 035
# HW 06, October 11, 2021



#1a
def hasFinalLetter(strList,letters):
	allStringEndLetter = []
	for string in strList:
		if string[-1] in letters:
			allStringEndLetter.append(string)
	return  allStringEndLetter



#b
animals = ['cats','dogs', 'fish', 'birds', 'horse']
strOfLettersOne = 'soacSOAC'
print(hasFinalLetter(animals, strOfLettersOne))


brands = ['zara', 'icing', 'gucci']
strOfLettersTwo = 'AHYahy'
print(hasFinalLetter(brands, strOfLettersTwo))

fruits = ['apple', 'blueberry', 'orange']
strOfLettersThree = 'ZXDzxd'
print(hasFinalLetter(fruits, strOfLettersThree))


#2a


def isDivisible(maxInt,twoInts):
	divisible = []
	listOfNumbers = range(1,maxInt)
	for num in listOfNumbers:
		if num % twoInts[0] == 0 and num % twoInts[-1] == 0:
			divisible.append(num)
	return divisible

#b
intTest1 = 100
twoDivisibleNumbers = (4,10)
print(isDivisible(intTest1, twoDivisibleNumbers))

intTest2= 36
twoDivisibleNumbers2 = (6,4)
print(isDivisible(intTest2, twoDivisibleNumbers2))

intTest3 = 55
twoDivisibleNumbers3 = (7,8)
print(isDivisible(intTest3, twoDivisibleNumbers3))









