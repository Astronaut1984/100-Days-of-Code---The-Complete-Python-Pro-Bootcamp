from screen import GameScreen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

sc = GameScreen()
score = ScoreBoard()
sc.draw_border()
score.draw_score(0, 0)
player1 = Paddle(360)
player2 = Paddle(-360)


def main():

    sc.bind_keys(["Up", "Down", "w", "s"])
    actions = {
        "Up": player1.up,
        "Down": player1.down,
        "w": player2.up,
        "s": player2.down,
    }

    ball = Ball()

    while True:
        player_didnt_score = True
        if sc.pressed_keys:
            while player_didnt_score:
                for key in sc.pressed_keys:
                    actions[key]()
                ball.move()
                winner = ball.check_collision([player1, player2])
                if winner is not None:
                    handle_winner(winner)
                    player_didnt_score = False
                sc.update()
                time.sleep(1 / 60)
            ball.reset()
        sc.update()
        time.sleep(1 / 60)
    sc.screen.exitonclick()
    pass


def handle_winner(winner):
    if winner == 1:
        player1.score += 1
    elif winner == 2:
        player2.score += 1
    score.draw_score(p1_score=player1.score, p2_score=player2.score)


if __name__ == "__main__":
    main()
