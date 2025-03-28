from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.color("green")
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("black")
        self.write(f"GAME OVER", align="center", font=("Courier", 40, "normal"))

    def detect_end(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
