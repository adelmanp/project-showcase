
import random
import logging
from turtle import Turtle


logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.setheading(random.randrange(1, 361))

    def move(self):
        new_x = self.xcor() + self.x_move
        logger.debug(f"Ball:: move(): new_x = {new_x}")
        new_y = self.ycor() + self.y_move
        logger.debug(f"Ball:: move(): new_y = {new_y}")
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.bounce_x()
        self.move_speed = 0.1
        self.goto(0, 0)
        self.color('white')
