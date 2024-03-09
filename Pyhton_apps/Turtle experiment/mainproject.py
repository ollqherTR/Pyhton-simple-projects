from turtle import Turtle , Screen
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def random_circle():
    for x in range(10):
        tupple=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

        timmy.showturtle()
        timmy.dot(20,tupple)
        timmy.hideturtle()
        timmy.forward(30)
    timmy.left(90)
    
    timmy.forward(30)
    
    timmy.left(90)
    timmy.forward(30)
    for x in range(10):
        tupple=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

        timmy.showturtle()
        timmy.dot(20,tupple)
        timmy.hideturtle()
        timmy.forward(30)
        
    timmy.right(90)
    timmy.forward(30)
    timmy.right(90)
    timmy.forward(30)
    



screen=Screen()
screen.colormode(255)
timmy.hideturtle()
timmy.penup()
timmy.pensize(1)
timmy.speed("fastest")
timmy.right(135)
timmy.forward(200)
timmy.right(225)
for y in range(5):
    random_circle()
    



screen.exitonclick()