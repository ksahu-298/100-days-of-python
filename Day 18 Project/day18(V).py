#making a spirograph
import turtle
import random
turtle.colormode(255)
spirograph = turtle.Turtle()
spirograph.speed("fastest")
spirograph.pensize(3)
spirograph.hideturtle()

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spirograph.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        spirograph.circle(100)
        spirograph.setheading(spirograph.heading() + size_of_gap)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()