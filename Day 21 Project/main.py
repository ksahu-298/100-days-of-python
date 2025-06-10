from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake() #create a snake object
food = Food()  #create a food object
scoreboard = Scoreboard()  #create a scoreboard object  


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

# Check for collision with food
    if snake.head.distance(food) < 15:  # If the snake's head is close to the food
        food.refresh()  # Refresh the food position
        new_segment = Turtle("square")  # Create a new segment for the snake
        new_segment.color("white")
        new_segment.penup()
        snake.segments.append(new_segment)  # Add the new segment to the snake

 # Increase the score when food is eaten        
        scoreboard.increase_score() 
# Check for collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
# Check for collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()