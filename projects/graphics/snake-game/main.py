#!/usr/bin/python3


import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)


game_on = True
snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.snake_head.distance(food) < 15:
        food.food_drop()
        snake.extend_snake()
        score_board.increase_score()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

    # Detect collision with wall
    if snake.snake_head.xcor() > 285 or snake.snake_head.xcor() < -285 or snake.snake_head.ycor() > 285 or snake.snake_head.ycor() < -285:
        score_board.reset()
        snake.reset()


screen.exitonclick()
