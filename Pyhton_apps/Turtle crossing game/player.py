from turtle import Screen,Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player():
    def __init__(self) :
        self.player = Turtle()
        self.player.color("black")
        self.player.penup()
        self.player.hideturtle()
        self.go_start()
        self.player.left(90)
        self.player.shape("turtle")
        self.player.showturtle()



    def move(self):
        self.player.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.player.ycor()>FINISH_LINE_Y:
            return True
        else : 
            return False
    def go_start(self):
        self.player.goto(0,-280)