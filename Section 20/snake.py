from turtle import Turtle

BODY_LENGTH = 3
SEGMENT_WIDTH = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake: list[Turtle] = []
        for i in range(BODY_LENGTH):
            self.add_segment((-i * SEGMENT_WIDTH, 0))
        self.head = self.snake[0]

    def move(self):
        for seg_idx in range(len(self.snake) - 1, 0, -1):
            new_x, new_y = (
                self.snake[seg_idx - 1].xcor(),
                self.snake[seg_idx - 1].ycor(),
            )
            self.snake[seg_idx].teleport(new_x, new_y)
        self.head.forward(SEGMENT_WIDTH)

    def add_segment(self, position: tuple):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.speed("fastest")
        segment.pu()
        segment.teleport(*position)
        self.snake.append(segment)

    def clear(self):
        for segment in self.snake:
            segment.hideturtle()

    def grow(self):
        self.add_segment(self.snake[-1].position())
        pass

    def collide_self(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
