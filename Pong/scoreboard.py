from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.write_score()


    def update_lscore(self):
        self.l_score += 1
        self.write_score()

    def update_rscore(self):
        self.r_score +=1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(arg=self.l_score,align="center",font=("Arial",50,"normal"))
        self.goto(100,200)
        self.write(arg=self.r_score,align="center",font=("Arial",50,"normal"))
