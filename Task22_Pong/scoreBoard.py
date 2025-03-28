from turtle import Turtle


class ScoreBoard(Turtle):
    # initialize the attributes. It will execute prior to start the code.
    def __init__(self):
        # With this command it cna be used anything of the turtle class
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(-100, 200)
        self.hideturtle()
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

