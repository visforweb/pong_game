from turtle import Turtle
from score import Scoreboard_L
import random

SPEED = 15
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.8, .8)
        self.penup()
        self.color("orange")
        self.reset_pos()
        self.x_move = SPEED
        self.y_move = SPEED
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        print("hi")

    def rebound_x(self):
        self.x_move *= -1

    def rebound_y(self):
        self.y_move *= -1

    def reset_pos(self):
        random_x = random.randint(-200,200)
        random_y = random.randint(-200, 200)

        self.goto(random_x, random_y)


    def speed_up(self,a):
        if a>=0:
            new_x = self.xcor() + self.x_move*2
            new_y = self.ycor() + self.x_move *2
            self.goto(new_x, new_y)
            print("gajab")

    def increse_speed(self,a):
        if a >= 2:
            print("kaam kiya")
            return True

        print("gajab")


