from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,location):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.speed(0)
        self.goto(x=location,y=0)

    def move_up(self):
        y = self.ycor()
        y += 20  # Move up by 20 pixels
        self.goto(self.xcor(),y)

    def move_down(self):
        y = self.ycor()
        y -= 20  # Move down by 20 pixels
        self.goto(self.xcor(),y)