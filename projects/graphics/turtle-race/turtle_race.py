#!/usr/bin/python3

from turtle import Turtle, Screen
import random

is_race_on = False
bet = True
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_position = 160

while bet:
    user_bet = screen.textinput(title='Place your bet', prompt='Which turtle '
                                'will win the race? Enter a color ("red", '
                                '"orange", "yellow", "green", "blue", '
                                '"purple"): ')
    if user_bet.lower() in colors:
        bet = False

# make turtles
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position)
    y_position -= 60
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
