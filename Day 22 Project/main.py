from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Turns off the screen updates for better performance
screen.setup(width=800, height=600)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

ball = Ball()
scores=Scoreboard()

# Keyboard bindings
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while True:
    time.sleep(ball.move_speed)  # Control the speed of the game
    screen.update()
    ball.move()
 
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddles
    if (ball.xcor() > 320 and ball.xcor() < 340) and (ball.distance(r_paddle) < 50):
        ball.bounce_x()
    elif (ball.xcor() < -320 and ball.xcor() > -340) and (ball.distance(l_paddle) < 50):
        ball.bounce_x()
    
    # Detect when the ball goes out of bounds
    if ball.xcor() > 390 : # Right boundary
             scores.l_point()
             ball.reset_position()  # Reset the ball to the center
             ball.bounce_x()  
    if ball.xcor() < -390: # Left boundary
            scores.r_point()
            ball.reset_position()  # Reset the ball to the center 
            ball.bounce_y()  # Reverse the ball's direction
        
        





screen.exitonclick()
