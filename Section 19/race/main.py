from turtle import Turtle, Screen
import random


def main():
    screen = Screen()
    screen.setup(width=500, height=400)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles: list[Turtle] = []
    for color in colors:
        turt = Turtle(shape="turtle")
        turt.color(color)
        turt.penup()
        turtles.append(turt)

    for i, turt in enumerate(turtles):
        turt.teleport(-230, 160 - (63 * i))

    user_bet = screen.textinput(
        title="Place your bets", prompt="Who will win? Enter a color: "
    )

    winner = ""
    finish_line = int((screen.window_width() // 2) - 20)
    while winner == "":
        for turt, color in zip(turtles, colors):
            x, _ = turt.position()
            if x >= finish_line:
                winner = color
                break
            dist = random.randrange(start=5, stop=20)
            turt.forward(dist)

    if winner == user_bet:
        print(f"You've won! The {winner} turtle is the winner!")
    else:
        print(f"You've lost! The {winner} turtle is the winner!")

    screen.exitonclick()


if __name__ == "__main__":
    main()
