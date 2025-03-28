from turtle import Screen
from food import Food
import time
from snake import SnakeSetup
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("The snake game 1994")
screen.tracer(0)

# Create snake object from the class
snake = SnakeSetup()
food = Food()
scoreboard = ScoreBoard()

# Update the screen with all configurations
SnakeSetup.setup_screen(snake)

# Set up the keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# While the game is on, update the movements
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Function to move the snake
    SnakeSetup.move_update(snake)

    # Detect a collision with the food
    if snake.all_segments[0].distance(food) < 15:
        food.new_position()
        scoreboard.update_score()
        snake.extend()

    # Detect a collision with the wall
    if snake.all_segments[0].xcor() > 380 or snake.all_segments[0].xcor() < -400 or snake.all_segments[0].ycor() > 400 \
            or snake.all_segments[0].ycor() < -380:
        scoreboard.game_over()
        game_is_on = False
    # Detect a collision with itself
    for segment in snake.all_segments[1:]:
        if snake.all_segments[0].distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
