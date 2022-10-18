from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self) :
        self.line = Turtle()
        self.live_text = Turtle()
        self.level_text = Turtle()
        self.create_line()
        self.lives = 4
        self.level = 0
        
        self.level_text.hideturtle()
        self.level_text.penup()
        self.level_text.color("black")
        self.level_text.goto(-280,260)
        self.update_level()
        
        self.live_text.hideturtle()
        self.live_text.penup()
        self.live_text.color("black")
        self.live_text.goto(-275,240)
        self.update_lives()
    
    
    def create_line(self):
        self.line.hideturtle()
        self.line.pensize(3)
        self.line.penup()
        self.line.color("black")
        self.line.goto(-300,230)
        self.line.pendown()
        for i in range(30):
            self.line.forward(10)
            self.line.penup()
            self.line.forward(10)
            self.line.pendown()
        # self.finish.hideturtle()
        # self.finish.penup()
        # self.finish.color("black")
        # self.finish.goto(0,230)
        # self.finish.write("Finish", False, align="center", font=("Arial", 20, "normal"))
        
        
    def update_level(self):
        self.level +=1
        self.level_text.clear()
        self.level_text.write(f"Level: {self.level}", False, align="left", font=FONT)
        
        
    def update_lives(self):
        self.lives -=1
        self.live_text.clear()
        self.live_text.write(f"Lives: {self.lives}", False, align="left", font=("Courier", 12, "normal"))
        
    def game_over(self):
        self.over = Turtle()
        self.over.hideturtle()
        self.over.color("Black")
        self.over.write("GAME OVER", align="center", font=FONT)