from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake() #create a snake object
screen.listen() #listen for key presses
screen.onkey(snake.up, "Up")  # Bind the up arrow key to the snake's up method
screen.onkey(snake.down, "Down")  # Bind the down arrow key to the snake's down method
screen.onkey(snake.left, "Left")  # Bind the left arrow key to the snake's left method
screen.onkey(snake.right, "Right")  # Bind the right arrow key to the snake's right method


game_is_on = True
while game_is_on:
    screen.update() #update the animation & group snake as 1 object
    time.sleep(0.1)  # Adjust the speed of the game as needed    


    snake.move()  # Move the snake forward
















screen.exitonclick()