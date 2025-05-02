# random walks using turtle module
from turtle import Turtle, Screen
import random

walker = Turtle()
walker.shape("turtle")

color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateBlue", "Wheat"]
direction = [0, 90, 180, 270]
walker.speed("fastest")
walker.pensize(15
               )
for _ in range(200):
    walker.color(random.choice(color))
    walker.pensize(10)
    walker.forward(30)
    walker.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()