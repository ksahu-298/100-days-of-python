#creating a square using turtle library

from turtle import Turtle , Screen
square = Turtle()
square.shape("turtle")
square.color("green")

for _ in range(4):
    square.left(90)
    square.forward(100)

screen = Screen()
screen.exitonclick()

import heroes
# pip install heroes - to install heroes library
print(heroes.gen())