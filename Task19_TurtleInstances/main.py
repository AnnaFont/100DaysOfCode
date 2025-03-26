import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=500)

user_bet = screen.textinput("Make your bet", "Who will win the race?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coord = -100
all_turtles = []

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coord)
    y_coord = y_coord + 35
    all_turtles.append(new_turtle)

in_race = False
if user_bet:
    in_race = True

winner = "None"
while in_race:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            in_race = False
            winner = turtle.pencolor()

print(f"The winner is {winner}")
if winner == user_bet:
    print("You have win")
else:
    print("You have lost")

screen.exitonclick()
