from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "W")
screen.onkey(paddle_left.go_down, "S")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()



    #Ball out of field
    if ball.xcor() > 350:
        ball.restart()
        ball.paddle_bounce()
        scoreboard.l_point()

    if ball.xcor() < -350:
        ball.restart()
        ball.paddle_bounce()
        scoreboard.r_point()

screen.exitonclick()