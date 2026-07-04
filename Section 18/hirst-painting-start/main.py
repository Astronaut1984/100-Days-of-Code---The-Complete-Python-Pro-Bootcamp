import colorgram
import random
from turtle import Turtle, Screen


def check_white(rgb_color):
    r = rgb_color.r
    g = rgb_color.g
    b = rgb_color.b

    if r >= 230 and g >= 230 and b >= 230:
        return None
    return (r, g, b)


def extract_colors(image_path, num_colors):
    rgb_colors = []
    colors = colorgram.extract(image_path, num_colors)
    for color in colors:
        rgb_color = color.rgb
        color_tuple = check_white(rgb_color)
        if color_tuple is not None:
            rgb_colors.append(color_tuple)
    return rgb_colors


def draw_point(rgb_colors: list[tuple], tim: Turtle):
    color = random.choice(rgb_colors)
    tim.color(tuple(v / 255 for v in color))
    tim.dot(size=20)


def main():
    rgb_colors = extract_colors("image.jpg", 30)

    tim = Turtle()
    tim.speed(0)
    tim.teleport(-300, -300)
    tim.hideturtle()
    tim.pu()

    for i in range(10):
        for _ in range(10):
            draw_point(rgb_colors, tim)
            tim.forward(60)
        tim.teleport(-300, -300 + ((i + 1) * 60))
    s = Screen()
    s.exitonclick()


if __name__ == "__main__":
    main()
