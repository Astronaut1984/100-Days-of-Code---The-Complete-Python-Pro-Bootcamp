from turtle import Screen, Turtle


class GameScreen:
    def __init__(self, width=800, height=450):
        self.screen = Screen()
        self.width = width
        self.height = height
        self.screen.setup(width=self.width, height=self.height)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.listen()
        self.pressed_keys = set()
        pass

    def draw_border(self):
        border_tim = Turtle()
        border_tim.hideturtle()
        border_tim.teleport(x=0, y=self.height / 2)
        border_tim.seth(270)
        border_tim.color("white")
        border_tim.width(3)
        while border_tim.ycor() > -self.height / 2:
            border_tim.forward(10)
            border_tim.pu()
            border_tim.forward(10)
            border_tim.pd()
        self.update()

    def bind_keys(self, keys: list):
        for key in keys:
            self.screen.onkeypress(
                fun=lambda key=key: self.pressed_keys.add(key), key=key
            )
            self.screen.onkeyrelease(
                fun=lambda key=key: self.pressed_keys.discard(key), key=key
            )

    def start(self):
        self.screen.exitonclick()

    def update(self):
        self.screen.update()
