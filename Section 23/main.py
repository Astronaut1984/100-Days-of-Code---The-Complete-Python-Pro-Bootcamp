import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.listen()
    screen.tracer(0)
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()
    screen.onkeypress(key="Up", fun=player.move)

    game_is_on = True
    while game_is_on:
        car_manager.create_car()
        car_manager.move_cars()
        car_manager.cleanup()
        if player.check_collision(car_manager.cars):
            game_is_on = False
        if player.check_won():
            player.reset_pos()
            car_manager.speedup()
            scoreboard.level_up()
        time.sleep(0.1)
        screen.update()
    scoreboard.draw_game_over()
    screen.exitonclick()


if __name__ == "__main__":
    main()
