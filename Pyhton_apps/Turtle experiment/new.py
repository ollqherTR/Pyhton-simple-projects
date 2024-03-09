from turtle import Turtle , Screen
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def random_circle():
    timmy.circle(120)
    timmy.left(5)





screen=Screen()

screen.colormode(255)
timmy.pensize(1)
timmy.speed("fastest")
for y in range(360):
   
    tupple=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  
    timmy.pencolor(tupple)
    random_circle()



screen.exitonclick()