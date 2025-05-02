# to draw a dotted line
from turtle import Turtle, Screen

karan = Turtle()

for _ in range(15):
    karan.forward(10)
    karan.penup()
    karan.forward(10)
    karan.pendown()

screen = Screen()
screen.exitonclick()