from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.start()
    
    
    def start(self):
        self.hideturtle()
        self.goto(0,-200)
        self.showturtle()
        
    def move_up(self):
        self.forward(10)
