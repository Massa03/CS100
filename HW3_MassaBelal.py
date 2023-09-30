# Massa Belal
# CS 100 2021F Section 035
# HW 03, September 20, 2021

#1

import turtle
import math

#Triangle
bob = turtle.Turtle()
bob.pendown()
bob.forward(100)
bob.left(120)
bob.forward(100)
bob.left(120)
bob.forward(100)
bob.left(120)

#Square
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

#pentagon
bob.right(72)
bob.forward(100)
bob.left(72)
bob.forward(100)
bob.left(72)
bob.forward(100)
bob.left(72)
bob.forward(100)
bob.left(72)
bob.forward(100)


#2
#circle

bob.penup()
bob.forward(200)
bob.pendown()
bob.circle(50)
bob.penup()
bob.right(90)
bob.forward(50)
bob.left(90)
bob.pendown()
bob.circle(100)
bob.penup()
bob.right(90)
bob.forward(50)
bob.left(90)
bob.pendown()
bob.circle(150)
bob.penup()
bob.right(90)
bob.forward(50)
bob.left(90)
bob.pendown()
bob.circle(200)

#3
#a
factorial_of_100= math.factorial(100)
print(factorial_of_100)

#b
logarithm = math.log2(1000000)
print(logarithm)

#c
greatest_common_divisor = math.gcd(63,49)
print(greatest_common_divisor)

