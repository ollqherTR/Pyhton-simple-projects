import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
play=Player()
car =CarManager()
scor=Scoreboard()
game_is_on = True

screen.onkey(play.move,"Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    for cars in car.all_cars:
        if cars.distance(play.player)<20:
            scor.game_is_over()
            game_is_on =False

    play.finish_line()
    if play.finish_line():
        play.go_start()
        car.level_up()
        scor.update_level()


screen.exitonclick()