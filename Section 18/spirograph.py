from turtle import Turtle, Screen
import random


def rand_color(turtle: Turtle):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r, g, b))


def draw_circle(tim: Turtle, radius, angle):
    rand_color(tim)
    tim.circle(radius)
    tim.right(angle)


def main():
    tim = Turtle()
    s = Screen()
    tim.speed(0)
    tim.pensize(3)

    radius = 100
    angle = 10
    num_circles = int(360 / angle)

    for _ in range(num_circles):
        draw_circle(tim, radius, angle)
    s.exitonclick()


if __name__ == "__main__":
    main()
