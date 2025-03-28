from turtle import Screen
from paddle import PaddleClass
from ball import BallClass
from scoreBoard import ScoreBoard
import time

SCREEN_SIZE_X = 450
SCREEN_SIZE_Y = 280
move_speed = 0.1

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

screen.listen()

r_paddle = PaddleClass((SCREEN_SIZE_X, 0))
l_paddle = PaddleClass((-SCREEN_SIZE_X, 0))
ball = BallClass()
score = ScoreBoard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with the wall
    if ball.ycor() > SCREEN_SIZE_Y-5 or ball.ycor() < -SCREEN_SIZE_Y+5:
        ball.bounce_y()

    # Collision with the paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > SCREEN_SIZE_X-40 or ball.distance(l_paddle) < 30 \
            and ball.xcor() < -SCREEN_SIZE_X+40:
        ball.bounce_x()

    # Detect when paddle right miss the wall
    if ball.xcor() > SCREEN_SIZE_X-10:
        ball.reset_position()
        score.l_point()
        move_speed = 0.1

    # Detect when paddle left miss the wall
    if ball.xcor() < -SCREEN_SIZE_X+10:
        ball.reset_position()
        score.r_point()