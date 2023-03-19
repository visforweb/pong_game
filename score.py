from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard_L(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-350, 230)
        self.color("white")
        self.score = 0
        self.write(f"Score : {self.score}",font= FONT, align="left")
        self.hideturtle()



    def score_checker(self):
        """this increases the score by 1"""
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}",  font=FONT, align="left")


    def display_gameover(self):
        self.penup()
        self.goto(-30, 0)
        self.color("red")
        self.write(f"Game Over", font=('Arial', 25, 'bold'))


