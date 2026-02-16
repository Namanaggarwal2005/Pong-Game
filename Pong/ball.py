from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.color("white")
        self.shape("circle")
        self.del_x = 10
        self.del_y = 10
        

    def move(self):
        new_x = self.xcor()+self.del_x
        new_y = self.ycor()+self.del_y
        self.penup()
        
        self.goto(new_x,new_y)

    def bounce_up(self):
        self.del_y *= -1 

    def bounce_paddle(self):
        self.del_x *= -1 
        
    