#Python Turtle - WordArt Challenge - https://www.101computing.net/python-turtle-wordart-challenge/
import turtle
import random
import time
from alphabet import alphabet

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(1)
window = turtle.Screen()
window.bgcolor("#000000")
myPen.pensize(2)

def displayMessage(message,fontSize,color,x,y):
  myPen.color(color)
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen.pendown()
        
      x += fontSize
      
    if character == " ":
      x += fontSize
    x += characterSpacing 

#Main Program Starts Here
fontSize = 10
characterSpacing = 5
fontColor = "white"

for i in range(2):
	if i == 0:
		message = 'Prepare se algo incrvel esta prestes a acontecer..................'
	elif i== 1:
		fontSize = 30
		time.sleep(3)
		myPen.speed(10)
		myPen.pensize(5)
		fontColor = "red"
		message = 'vem de boquinha seu merda UUUUHUHUHhhhhhhhhhhhhhhhhh...............'

	displayMessage(message,fontSize,fontColor,-600,0)
	myPen.clear()
	# time.sleep(10)

