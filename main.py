from turtle import Turtle, Screen
import time
from padd import Paddle
from food import Ball
from score import Scoreboard_L
from life import Life_l
score = Scoreboard_L()
life = Life_l()
screen = Screen()
screen.setup(900, 600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)
screen.listen()
paddle = Paddle()
ball = Ball()
screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)

    ball.move()

    if ball.xcor() > 430 or ball.xcor() < -430:
        ball.rebound_x()
    if ball.ycor() > 280:
        ball.rebound_y()

    if ball.ycor() <= -260:
      if ball.distance(paddle.segments[1])<50 or ball.distance(paddle.segments[0]) <20  or ball.distance(paddle.segments[2])<20:
         ball.rebound_y()
         score.score_checker()
         for i in range(0,10,1):
          if score.score ==i+1:
            ball.x_move *= (i*.10+1)
            ball.y_move *= (i*.10+1)


      elif ball.ycor() < -270 and ball.distance(paddle.segments[1]) >270:
         life_checker()

         if life.lives == 0:
            game_on = False
            life.display_gameover()


screen.exitonclick()






