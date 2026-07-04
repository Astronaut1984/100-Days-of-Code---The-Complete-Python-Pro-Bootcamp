from turtle import Turtle

PADDLE_HEIGHT = 4  # multiples of 20px -> 80px tall
PADDLE_WIDTH = 1  # multiples of 20px -> 20px wide
MOVE_DISTANCE = 5
Y_BOUND = 180  # keep paddle within screen (tweak to your height)


class Paddle(Turtle):
    def __init__(self, xcor=360):
        super().__init__(shape="square")
        self.shapesize(stretch_len=PADDLE_WIDTH, stretch_wid=PADDLE_HEIGHT)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.teleport(xcor, 0)
        self.score = 0

    def up(self):
        if self.ycor() < Y_BOUND:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -Y_BOUND:
            self.sety(self.ycor() - MOVE_DISTANCE)
