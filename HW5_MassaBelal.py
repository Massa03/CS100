# Massa Belal
# CS 100 2021F Section 035
# HW 05, October 4, 2021

#1
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months:
    if month[0] == 'J':
        print(month)

#2
for number in range(0,100):
    if number % 2 == 0 and number % 5 == 0:
        print(number)

#3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
with_vowels = 0

for word in horton:
    if word  in vowels:
        print(word)

   
