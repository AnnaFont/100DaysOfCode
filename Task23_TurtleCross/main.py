import time
from turtle import Screen
from player import Player
from car_manager import CarManager

from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect a collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            # Car collision - game over
            player.game_over()
            game_is_on = False

    # Detect reach to the end
    if player.detect_end():
        player.go_to_start()
        # Finish at the end - go to start pos and increase speed
        car_manager.reset_game()
        ScoreBoard.increase_level(scoreboard)
    ScoreBoard.update_scoreboard(scoreboard)

screen.exitonclick()

