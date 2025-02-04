from turtle import Turtle

from setuptools.windows_support import hide_file

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self, height):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as readfile:
            self.high_score = int(readfile.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety((height / 2) - 30)
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as writefile:
                writefile.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', move=False, align="center", font=FONT)

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER.", move=False, align="center", font=FONT)
