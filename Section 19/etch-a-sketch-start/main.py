from turtle import Turtle, Screen


def move_forwards(tim: Turtle):
    tim.forward(10)


def move_backwards(tim: Turtle):
    tim.back(10)


def turn_right(tim: Turtle):
    tim.right(10)


def turn_left(tim: Turtle):
    tim.left(10)


def clear(tim: Turtle):
    tim.clear()
    tim.teleport(0, 0)


def main():
    tim = Turtle()
    sc = Screen()

    sc.listen()
    sc.onkey(key="w", fun=lambda: move_forwards(tim))
    sc.onkey(key="s", fun=lambda: move_backwards(tim))
    sc.onkey(key="d", fun=lambda: turn_left(tim))
    sc.onkey(key="a", fun=lambda: turn_left(tim))
    sc.onkey(key="c", fun=lambda: clear(tim))

    sc.exitonclick()


if __name__ == "__main__":
    main()
