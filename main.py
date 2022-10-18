import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()


player = Player()
screen.onkey(player.move_up, "Up")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_cars()
    for car in car_manager.cars:
        if player.distance(car) < 25:
            player.start()
            scoreboard.update_lives()
        
    if player.ycor() > 229:
        player.start()
        scoreboard.update_level()
        car_manager.increase_level()
        
    if scoreboard.lives < 0:
        game_is_on = False
        
scoreboard.game_over()
    
screen.exitonclick()