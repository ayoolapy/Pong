from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.goto(-80, 235)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))
        self.goto(80, 235)
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update()