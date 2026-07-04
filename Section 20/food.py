from turtle import Turtle
import random

SCREEN_WIDTH = 280
SCREEN_HEIGHT = 260


class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.move()

    def move(self):
        new_x = 0
        new_y = 0
        while (new_x, new_y) == self.pos():
            new_x = random.randrange(-SCREEN_WIDTH, SCREEN_WIDTH, 20)
            new_y = random.randrange(-SCREEN_WIDTH, SCREEN_HEIGHT, 20)
        self.teleport(new_x, new_y)
