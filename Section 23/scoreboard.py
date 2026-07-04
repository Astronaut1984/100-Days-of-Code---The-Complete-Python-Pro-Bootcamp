from turtle import Turtle

FONT = ("Courier", 24, "bold")
LEVEL_POSITION = (-290, 260)
GAME_OVER_POSITION = (0, 100)


class Scoreboard(Turtle):
    def __init__(self, shape="classic", undobuffersize=1000, visible=False):
        super().__init__(shape, undobuffersize, visible)
        self.level = 1
        self.teleport(*LEVEL_POSITION)
        self.draw_level()

    def level_up(self):
        self.level += 1
        self.draw_level()

    def draw_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT, align="left")

    def draw_game_over(self):
        self.teleport(*GAME_OVER_POSITION)
        self.write(arg="GAME OVER", font=FONT, align="center")
