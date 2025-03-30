from turtle import Turtle
import time

# Absolute file path
PATH_RESULTS_ABS = "/Users/annafontllenas/Documents/GitHub/100DaysOfCode/Task24_Snake"

# Relative file path - 1 step up use ./ - 2 steps up use ../
PATH_RESULTS_REL = "./"

class ScoreBoard(Turtle):
    # initialize the attributes. It will execute prior to start the code.
    def __init__(self):
        # With this command it cna be used anything of the turtle class
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 350)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 350)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
        self.goto(0, 0)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def count_down(self):
        self.update_scoreboard()
        self.write("3", align="center", font=("Courier", 200, "normal"))
        time.sleep(0.5)
        self.update_scoreboard()
        self.write("2", align="center", font=("Courier", 200, "normal"))
        time.sleep(0.5)
        self.update_scoreboard()
        self.write("1", align="center", font=("Courier", 200, "normal"))
        time.sleep(0.5)
        self.update_scoreboard()
        self.write("GO!", align="center", font=("Courier", 200, "normal"))
        time.sleep(0.5)
        self.goto(0, 350)
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
        self.score_doc_write()
        self.count_down()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER :(", align="center", font=("Courier", 40, "normal"))

    def score_doc_read(self):
        # Save high score in a file. a -> append
        path = PATH_RESULTS_ABS + "/data_file.txt"
        # Same as using: with open("data_file.txt", mode="r") as results_file:
        with open(path, mode="r") as results_file:
            self.high_score = int(results_file.read())
        self.update_scoreboard()

    def score_doc_write(self):
        # Save high score in a file. a -> append
        with open("data_file.txt", mode="w") as results_file:
            results_file.write(str(self.high_score))
