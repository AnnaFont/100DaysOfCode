from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def add_segment(position):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    return new_segment


class SnakeSetup:
    # initialize the attributes. It will execute prior to start the code.
    def __init__(self):
        self.all_segments = []

    def setup_screen(self):
        # Create snake body
        for segment in [1, 2, 3]:
            position = ((segment-1)*(-20), 0)
            self.all_segments.append(add_segment(position))

    def extend(self):
        seg_num = len(self.all_segments)-1
        position = (self.all_segments[seg_num].xcor(), self.all_segments[seg_num].ycor())
        self.all_segments.append(add_segment(position))

    def move_update(self):
        # Start with the segment 2 later 1 and finally 3 - move one position for each segment
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            self.all_segments[seg_num].goto(self.all_segments[seg_num - 1].xcor(),
                                            self.all_segments[seg_num - 1].ycor())
        self.all_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # If it is going down it cannot go down after
        if self.all_segments[0].heading() != DOWN:
            self.all_segments[0].setheading(90)

    def down(self):
        if self.all_segments[0].heading() != UP:
            self.all_segments[0].setheading(270)

    def left(self):
        if self.all_segments[0].heading() != RIGHT:
            self.all_segments[0].setheading(180)

    def right(self):
        if self.all_segments[0].heading() != LEFT:
            self.all_segments[0].setheading(0)
