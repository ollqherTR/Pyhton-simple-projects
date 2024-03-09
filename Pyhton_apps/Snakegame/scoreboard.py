from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("phyton_dersler/Snakegame/data.txt") as data:
            self.high_score =int(data.read())
        self.color("white")
        
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score is: {self.score} High Score : {self.high_score}", align="center", font=("Ariel",24,"normal"))

    def score_up(self):
        self.score += 1
        self.clear()  
        self.write_score()  
    def reset(self):
        if self.score> self.high_score:
            self.high_score =self.score
            with open("phyton_dersler/Snakegame/data.txt", mode="w") as highscore:
              highscore.write(f"{self.score}")
        self.score =0
        self.write_score()    