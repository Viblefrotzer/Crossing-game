import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "w")

game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.075)
    screen.update()
    random_chance = random.randint(1, 3)
    if random_chance == 1:
        car_manager.create_new_car()
    car_manager.moving()

    # # detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    # deleting cars out of the game
    for car in car_manager.all_cars:
        if car.xcor() < -340:
            car.ht()
            car_manager.all_cars.remove(car)

    # detect finish crossing
    if player.ycor() > 270:
        player.goto(0, -280)
        car_manager.new_level()
        scoreboard.new_level()

screen.exitonclick()
