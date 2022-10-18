from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
COLORS *= 4
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.speed = STARTING_MOVE_DISTANCE

    
    def create_cars(self):
        for i in COLORS:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=1.5)
            new_car.hideturtle()
            new_car.penup()
            new_car.color(i)
            new_car.setheading(180)
            new_car.goto(random.randint(50,800), random.randint(-140,190))
            new_car.showturtle()
            self.cars.append(new_car)
            
    
    def generate_cars(self):
        for i in self.cars:
            i.forward(self.speed)
            if i.xcor() < -330:
                self.respawn(i)
    
    
    def respawn(self,car):
        car.goto(random.randint(350,1100), random.randint(-140,190))
        
    def increase_level(self):
        self.speed += MOVE_INCREMENT