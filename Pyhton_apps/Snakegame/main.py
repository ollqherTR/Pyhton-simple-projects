from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake
screen =Screen()
screen.setup(600,600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

snake =Snake()
food =Food()
scoreboard=Scoreboard()
scoreboard.write_score()
screen.listen()
screen.onkey(snake.up ,"Up" )
screen.onkey(snake.down ,"Down" )
screen.onkey(snake.left ,"Left" )
screen.onkey(snake.right ,"Right" )

game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_up()
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() >280:
        scoreboard.reset()
        snake.reset()
       
    
    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
              scoreboard.reset()
              snake.reset()
              
        




screen.exitonclick()