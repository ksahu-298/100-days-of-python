#Etch-a-sketch
from turtle import Turtle, Screen

canvas= Turtle()
screen= Screen()
screen.title("Etch-a-sketch")
canvas.pensize(5)
canvas.color("blue")

def move_forward():
    canvas.forward(10)

def move_backward():
    canvas.backward(10)

def turn_left():
    canvas.left(10)

def turn_right():
    canvas.right(10)

def clear():
    canvas.clear()
    canvas.penup()
    canvas.home()
    canvas.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()