import random
from turtle import Turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_LOWER_BOUND = -240
CAR_UPPER_BOUND = 260

class CarManager:
    def __init__(self):
        self.cars = []
        self.inactive_cars = []
        self.last_spawn = time.time()
        self.spawn_interval = random.uniform(0.3, 0.8)
        self.move_dist = STARTING_MOVE_DISTANCE
        self.car_spawn_rate = 8
        self.car_increment = 0

    def create_car(self):
        if self.car_increment >= self.car_spawn_rate:
            if self.inactive_cars:
                car = self.inactive_cars.pop()
                car.use_new_location()
                car.showturtle()
                self.cars.append(car)
            else:
                car = Car()
                self.cars.append(car)
            self.car_increment = 0
        else:
            self.car_increment += 1

    def speedup(self):
        self.move_dist += MOVE_INCREMENT
        self.car_spawn_rate = min(self.car_spawn_rate - 1, 3)

    def move_cars(self):
        for car in self.cars:
            car.move(self.move_dist)

    def cleanup(self):
        survivors = []
        for car in self.cars:
            if car.xcor() < -300:
                car.hideturtle()
                self.inactive_cars.append(car)
            else:
                survivors.append(car)
        self.cars = survivors


class Car(Turtle):
    def __init__(self, shape="square", undobuffersize=1000, visible=True):
        super().__init__(shape, undobuffersize, visible)
        self.shapesize(1, 2)
        self.seth(180)
        self.color(random.choice(COLORS))
        self.pu()
        self.use_new_location()

    def use_new_location(self):
        y_pos = random.randrange(CAR_LOWER_BOUND, CAR_UPPER_BOUND, 1)
        self.teleport(300, y_pos)

    def move(self, move_dist):
        self.forward(move_dist)
