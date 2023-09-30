# Massa Belal
# CS 100 2021F Section 035
# HW 04, September 28, 2021

#1
#a
a, b, c = 3, 4, 5

#b
if a<b:
    print("OK")
#c
if c<b:
    print("OK")
#d
if a + b==c:
    print("OK")
#e
if (a**2)+(b**2)==c**2:
    print("OK")

#2

if a<b:
    print("OK")
else:
    print("NOT OK")
if c<b:
    print("OK")
else:
    print("NOT OK")
if a + b==c:
    print("OK")
else:
    print("NOT OK")
if (a**2)+(b**2)==c**2:
    print("OK")
else:
    print("NOT OK")

#3
import turtle

color = input('color:')
line_width = int(input('line width:'))
line_length = int(input('line length:'))
shape = input('line, triangle, or square:')

s = turtle.Screen()
bob = turtle.Turtle()
bob.color(color)
bob.width(line_width)
bob.pendown()

if shape == 'line':
    bob.forward(line_length)

elif shape == 'triangle':
    bob.forward(line_length)
    bob.right(60)
    bob.forward(line_length)
    bob.right(60)
    bob.forward(line_length)

else:
    bob.forward(line_length)
    bob.right(90)
    bob.forward(line_length)
    bob.right(90)
    bob.forward(line_length)
    bob.right(90)
    bob.forward(line_length)
    

