#!/usr/bin/python3

import time
import logging
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

game_on = True
screen = Screen()
screen.setup(width=800, height=600)
screen.title('PONG')
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Has the ball hit the top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Has the ball made contact with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if R paddle missed
    if ball.xcor() > 350:
        ball.color('red')
        score_board.l_point()
        screen.update()
        time.sleep(1)
        ball.reset()

    # Detect if L paddle missed
    if ball.xcor() < -350:
        ball.color('red')
        score_board.r_point()
        screen.update()
        time.sleep(1)
        ball.reset()

screen.exitonclick()
