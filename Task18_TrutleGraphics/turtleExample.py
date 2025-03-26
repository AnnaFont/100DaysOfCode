# Python turtle to create a dot spot painting randomised
from turtle import Turtle, Screen
import random
import turtle as t

tim = t.Turtle()

# Tuple means is immutable
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r, g, b)
    return rand_color


tim.shape("turtle")
tim.color("green")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "yellow"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


for _ in range(50):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

tim.pensize(3)
tim.color("black")

# Next challenge, infinite circles
for _ in range(70):
    tim.circle(100)
    tim.setheading(tim.heading() + 10)

screen = Screen()
screen.exitonclick()