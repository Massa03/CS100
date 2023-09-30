# Massa Belal
# CS 100 2021F Section 035
# HW 01, September 9,2021


# Exercise 5b
days = 365
age = 18
week = 7

# Exercise 5c
pi = 3.14
weight = 120.5
money = 15.99

# Exercise 5d
graphing = 'Math'
cookWithoutLooking = 'Burak'
favoriteSubject = 'Algebra'


# Exercise 1.1

#1. Print without parenthesis gives a syntax error

#2. string without qoutation marks gives a name error

#3. 2++2 is equal to 4 and returns no errors

#4. Syntax error

#5. Syntax error

# Exercise 1.2
#1.

print((60 * 42) + 42)

#2.
print(10 / 1.61)

#3.
average_pace_in_seconds = 2562 / 6.2
print(average_pace_in_seconds / 60)
avrage_speed = 6.2 / 2562
print(avrage_speed)
# Exercise 2.1
# 1. 42 = n is illegal

#2. It is legal

#3. You can use semicolons but it is not necessary

#4. Syntax error

#5. You get a name error

# Exercise 2.2
#1.
print(((4 * 3.14 * (5**3)) / 3))

#2.
price_after_discount = ((24.95 - (24.95 * 0.4)))
print(price_after_discount)
shipping_cost = ((0.75 * 59) + 3)
print(shipping_cost)
price_without_shipping = price_after_discount * 60
print(price_without_shipping)
total_wholesale_cost = price_without_shipping + shipping_cost
print(total_wholesale_cost)

#3.
easy_pace = ((8 * 60)+ 15)* 2
tempo = ((7 * 60) + 12)  * 3
total_time_seconds = easy_pace + tempo
total_time_minutes = total_time_seconds / 60
total_time_sec = total_time_minutes * 60
print('0.',total_time_sec)
print('1.',total_time_minutes)
d_time = (6 * 60) + 52
print(d_time)
final_min = total_time_minutes + d_time
final_sec = final_min * 60
print(final_sec)
hour = final_min//60
hourS = hour*60*60
minutes = final_min %60
seconds = final_min * 60 % 60
print(hour,minutes,seconds)



