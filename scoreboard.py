from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, height):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety((height / 2) - 30)
        self.write(f'Score: {self.score}', move=False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', move=False, align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER.", move=False, align="center", font=FONT)
