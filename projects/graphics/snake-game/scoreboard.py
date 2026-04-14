
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./data/high_score.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 265)
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data/high_score.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
        self.goto(0, 0)

        # self.write("GAME OVER", move=False,
        #            align=ALIGNMENT, font=FONT)
