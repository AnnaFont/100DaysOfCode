from turtle import Turtle


class ScoreBoard(Turtle):
    # initialize the attributes. It will execute prior to start the code.
    def __init__(self):
        # With this command it cna be used anything of the turtle class
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 350)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER :(", align="center", font=("Courier", 40, "normal"))
