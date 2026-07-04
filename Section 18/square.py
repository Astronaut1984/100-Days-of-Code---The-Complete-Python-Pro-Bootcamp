from turtle import Turtle, Screen


def main():
    t = Turtle()


    t.color("white", "white")
    for _ in range(2):
        t.left(90)
        t.forward(50)
    t.right(180)

    t.color("red", "red")
    for _ in range(4):
        t.forward(100)
        t.right(90)

    s = Screen()
    s.exitonclick()


if __name__ == "__main__":
    main()
