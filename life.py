from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Life_l(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(220, 230)
        self.color("white")
        self.lives = 3

        self.write(f" Life: {self.lives}", font= FONT, align="left")

        self.hideturtle()


    def life_checker(self):
        """this reduces the life by 1"""
        self.clear()
        self.lives -= 1
        self.write(f" Life: {self.lives}", font= FONT, align="left")
        print("marra")

    def display_gameover(self):
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.write(f"Game Over!", font= FONT, align="center")

