#Python Turtle – Graphics Keyboard Commands
import turtle
from turtle import *

setup(500, 500)
Screen()
turtle = turtle.Turtle()
turtle.speed(0)
showturtle()


def up():
	turtle.setheading(90)
	turtle.forward(100)


def down():
	turtle.setheading(270)
	turtle.forward(100)


def left():
	turtle.setheading(180)
	turtle.forward(100)


def right():
	turtle.setheading(0)
	turtle.forward(100)


listen()
onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

mainloop()
