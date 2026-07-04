from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, shape="classic", undobuffersize=1000, visible=False):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.teleport(0, 180)

    def draw_score(self, p1_score, p2_score):
        self.clear()
        self.write(
            arg=f"{p1_score}\t{p2_score}",
            font=("Pong Score", 30, "normal"),
            align="center",
        )
