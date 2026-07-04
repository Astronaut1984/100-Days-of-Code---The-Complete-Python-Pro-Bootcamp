from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, shape="classic", undobuffersize=1000):
        super().__init__(shape, undobuffersize, visible=False)
        self.score = 0
        self.pu()
        self.color("white")
        self.teleport(x=0, y=270)
        self.speed("fastest")
        self.write_score()

    def write_score(self):
        self.write(
            align="center", font=("Consolas", 20, "bold"), arg=f"Score: {self.score}"
        )

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def draw_game_over(self):
        self.clear()
        self.teleport(-100, 100)
        self.pd()
        self.seth(0)
        self.begin_fill()
        for i in range(4):
            self.forward(200)
            self.right(90)
        self.fillcolor("white")
        self.end_fill()
        self.color("black")
        self.teleport(0, 50)
        self.write(align="center", font=("Consolas", 20, "bold"), arg=f"Game Over")
        self.teleport(0, -50)
        self.write_score()
