from turtle import Turtle , Screen
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
def draw_squre():
    for x in range(0,5):
        timmy.forward(100)
        timmy.left(72)
    for x in range(0,4):
        timmy.forward(100)
        timmy.left(90)    
def random_walk(x):
    if x==0:
       timmy.left(90)
       timmy.forward(20)
    elif x==1:
        timmy.left(90)
        timmy.left(90)
        timmy.forward(20)
    elif x==2:
        timmy.right(90)
        timmy.forward(20)
    else:
        timmy.forward(20)
screen=Screen()

screen.colormode(255)
timmy.pensize(10)
timmy.speed(10)
for y in range(200):
    t = random.randint(0,3)
    tupple=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  
    timmy.pencolor(tupple)
    random_walk(t)



screen.exitonclick()