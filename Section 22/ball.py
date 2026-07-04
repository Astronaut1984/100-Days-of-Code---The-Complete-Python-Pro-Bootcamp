from turtle import Turtle
import math
import random

Y_BOUND = 205
X_BOUND = 380


class Ball(Turtle):
    def __init__(self, shape="circle", undobuffersize=1000, visible=True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.speed("fastest")
        self.pu()
        self.reset()

    def move(self):
        new_x = self.xcor() + self.delta_x
        new_y = self.ycor() + self.delta_y

        self.teleport(new_x, new_y)

    def check_collision(self, players: list[Turtle]):
        if self.ycor() >= Y_BOUND or self.ycor() <= -Y_BOUND:
            self.delta_y *= -1
            return None
        if self.xcor() >= X_BOUND:
            return 1
        if self.xcor() <= -X_BOUND:
            return 2
        for player in players:
            x, y = self.get_distance(player)
            if x < 20 and abs(y) < 40:
                self.delta_x *= -1

                offset_ratio = y / 40  # -1.0 (bottom edge) to 1.0 (top edge)
                offset_ratio = max(
                    -1.0, min(1.0, offset_ratio)
                )  # clamp in case of overlap
                self.delta_y = offset_ratio * 8

    def get_distance(self, turtle: Turtle):
        """
        Returns the distance between x and y coordinates
        Unlike the normal distance method
        """
        dx = abs(self.xcor() - turtle.xcor())
        dy = self.ycor() - turtle.ycor()
        return dx, dy

    def reset(self):
        self.setpos(0, 0)
        x_dir = random.choice([1, -1])
        y_dir = random.choice([1, -1])
        self.delta_x = 5 * x_dir
        self.delta_y = 5 * y_dir
