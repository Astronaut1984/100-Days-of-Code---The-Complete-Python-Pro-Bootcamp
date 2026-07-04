from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def main():
    # Setup screen and turtle
    s = Screen()

    s.setup(width=600, height=600)
    s.title("Snake")
    s.bgcolor("black")
    s.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    s.listen()
    s.onkey(snake.up, "Up")
    s.onkey(snake.down, "Down")
    s.onkey(snake.left, "Left")
    s.onkey(snake.right, "Right")

    game_running = True
    while game_running:
        s.update()
        time.sleep(0.1)
        snake.move()

        # Detect Food Eaten
        if snake.head.distance(food.position()) < 15:
            food.move()
            snake.grow()
            scoreboard.update_score()

        # Detect Wall Collision
        if (
            snake.head.xcor() > 290
            or snake.head.xcor() < -290
            or snake.head.ycor() > 290
            or snake.head.ycor() < -290
        ):
            game_running = False
        
        # Detect Snake Collision
        if snake.collide_self():
            game_running = False

    snake.clear()
    food.hideturtle()
    scoreboard.draw_game_over()
    s.update()
    s.exitonclick()


if __name__ == "__main__":
    main()
