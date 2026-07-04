from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
CAR_WIDTH = 40
CAR_HEIGHT = 20
PLAYER_SIZE = 20


class Player(Turtle):
    def __init__(self, shape="turtle", undobuffersize=1000, visible=True):
        super().__init__(shape, undobuffersize, visible)
        self.reset_pos()
        self.pu()

    def reset_pos(self):
        self.seth(90)
        self.teleport(*STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def check_collision(self, cars):
        for car in cars:
            dx, dy = self.get_xy_dist(car)
            if dx <= (CAR_WIDTH / 2 + PLAYER_SIZE / 2) and dy <= (
                CAR_HEIGHT / 2 + PLAYER_SIZE / 2
            ):
                return True
        return False

    def check_won(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def get_xy_dist(self, car):
        return (abs(self.xcor() - car.xcor()), abs(self.ycor() - car.ycor()))
