from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPAWN_LIST = []
for i in range(-230, 230, 20):
    SPAWN_LIST.append(i)

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MOVE_DISTANCE = STARTING_MOVE_DISTANCE


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_new_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.goto(320, random.choice(SPAWN_LIST))
        self.all_cars.append(new_car)

    def moving(self):
        for car in self.all_cars:
            car.backward(MOVE_DISTANCE)

    def new_level(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE += MOVE_INCREMENT
