from turtle import Turtle, Screen
import random

directions = [
    0,
    90,
    180,
    270,
]


def move_rand(tim: Turtle):
    heading = random.choice(directions)
    tim.setheading(heading)
    r = random.random()
    g = random.random()
    b = random.random()
    tim.color((r, g, b))
    tim.forward(30)


tim = Turtle()
tim.pensize(5)
tim.speed(10)

for _ in range(100):
    move_rand(tim)

s = Screen()
s.exitonclick()