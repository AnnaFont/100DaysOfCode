from turtle import Turtle
import random


def random_color():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    return colors[random.randint(0, 5)]


class Food(Turtle):
    # initialize the attributes. It will execute prior to start the code.
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color(random_color())
        self.speed("fastest")
        food_cord_x = random.randint(-200, 200)
        food_cord_y = random.randint(-200, 200)
        self.goto(food_cord_x, food_cord_y)

    def new_position(self):
        food_cord_x = random.randint(-200, 200)
        food_cord_y = random.randint(-200, 200)
        self.color(random_color())
        self.goto(food_cord_x, food_cord_y)
