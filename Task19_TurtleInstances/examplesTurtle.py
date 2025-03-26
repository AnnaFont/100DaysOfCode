import random
from turtle import Turtle, Screen


screen = Screen()
tim = Turtle()

tim.shape("turtle")
tim.color("green")

def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(20)


def turn_right():
    tim.right(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
clear()
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
clear()

screen = Screen()
screen.exitonclick()