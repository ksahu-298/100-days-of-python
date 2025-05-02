#drawing shapes with turtle
from turtle import Turtle, Screen
import random
color = ["red", "green", "blue", "yellow", "black", "white", "orange", "violet", "brown", "grey", "pink", "purple", "cyan", "magenta"]
tim = Turtle()

#to print triangle
def draw_triangle():
    tim.color(random.choice(color))
    for _ in range(3):
        tim.forward(100)
        tim.right(120)

#to print square
def draw_square():
    tim.color(random.choice(color))
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

#to print pentagon
def draw_pentagon():
    tim.color(random.choice(color))
    for _ in range(5):
        tim.forward(100)
        tim.right(72)

#to print hexagon
def draw_hexagon():
    tim.color(random.choice(color))
    for _ in range(6):
        tim.forward(100)
        tim.right(60)   

#to print heptagon
def draw_heptagon():
    tim.color(random.choice(color))
    for _ in range(7):
        tim.forward(100)
        tim.right(51.42)

#to print octagon
def draw_octagon():
    tim.color(random.choice(color))
    for _ in range(8):
        tim.forward(100)
        tim.right(45)

#to print nonagon
def draw_nonagon():
    tim.color(random.choice(color))
    for _ in range(9):
        tim.forward(100)
        tim.right(40)

#to print decagon
def draw_decagon():
    tim.color(random.choice(color))
    for _ in range(10):
        tim.forward(100)
        tim.right(36)


draw_triangle()
draw_square()
draw_pentagon()
draw_hexagon()
draw_heptagon()
draw_octagon()
draw_nonagon()
draw_decagon()

# 2nd method to draw shapes using for loop

for i in range (3,11):
    angle = 360 / i
    tim.color(random.choice(color))
    for _ in range(i):
        tim.forward(100)
        tim.right(angle)