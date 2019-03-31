print ("Hello and welcome to word drawing")
text = input ("Enter your text you want to print:")
selectedcolour = input ("What colour would you like it?")
thick = input ("How thick would you like it? (min:1 max:100)")

import turtle
forward=turtle.forward
back=turtle.backward
right=turtle.right
left=turtle.left
pup=turtle.penup
pdown=turtle.pendown
colour=turtle.color
thickness=turtle.width

colour(selectedcolour)
thickness(thick)
pup()
left(180)
forward(400)
left(180)
pdown()

def space():
    pup()
    forward(100)
    pdown()

def a():
    for i in range(450): #this is an A
        forward(2)
        left(1)
    forward(140)
    right(180)
    forward(240)
    for i in range(90):
        forward(1)
        left(1)
    pup()
    forward(100)
    left(90)
    forward(25)
    right(90)
    pdown()

def b():
    left(90)
    forward(300)
    back(250)
    for i in range(180):
        forward(3)
        right(2)
    back(100)
    pup()
    right(90)
    forward(300)
    pdown()

def c():
    pup()
    forward(100)
    left(90)
    forward(50)
    right(90)
    pdown()
    right(135)
    for i in range(275):
        forward(2)
        right(1)
    pup()
    right(45)
    forward(200)
    left(90)
    forward(100)
    pdown()

draw = {" ":space, "a":a, "b":b, "c":c}

for letter in text:
    if letter in draw.keys():
        draw[letter]()