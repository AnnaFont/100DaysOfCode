import colorgram
import turtle as t
import random
from turtle import Screen

t.colormode(255)
tim = t.Turtle()
rgb_colors = []
colors = colorgram.extract('image.jpeg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)

tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, 111):
    tim.pendown()
    tim.dot(20, random.choice(rgb_colors))
    tim.penup()
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
