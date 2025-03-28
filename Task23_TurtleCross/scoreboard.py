FONT = ("Courier", 24, "normal")
from turtle import Turtle


class ScoreBoard(Turtle):
    # initialize the attributes. It will execute prior to start the code.
    def __init__(self):
        # With this command it cna be used anything of the turtle class
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-200, 250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()


