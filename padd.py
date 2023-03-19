from turtle import Turtle
STARTING_POSITIONS=[(-23,-275), (23,-275)]

class Paddle():
    def __init__(self):
        self.segments = []
        self.create_paddle()






    def create_paddle(self):
        head_paddle = Turtle("square")
        head_paddle.shapesize(stretch_wid=1.2, stretch_len=6.5)
        head_paddle.setheading(0)
        head_paddle.penup()
        head_paddle.goto(0,-268)
        head_paddle.color("blue")
        self.segments.append(head_paddle)
        self.add_wheels()


    def add_wheels(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("circle")
            new_segment.color("white")
            new_segment.shapesize(1)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)



    def right(self):
      for i in range(3):
         """moves the combined turtle to right"""
         self.segments[1].forward(15)
         self.segments[2].forward(15 )
         self.segments[0].forward(15 )


    def left(self):
      for i in range(3):
         """moves combined turtles to the left"""
         self.segments[1].backward(15 )
         self.segments[0].backward(15)
         self.segments[2].backward(15 )




