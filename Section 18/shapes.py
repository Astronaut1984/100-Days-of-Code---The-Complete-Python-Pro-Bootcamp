import turtle as t
import random

tim = t.Turtle()

# Every polygon has a sum of internal angles corresponding to the number of angles in said polygon
# Triangle has 3 angles and 180 degrees
# Square has 4 angles and 360 degrees
# So it should follow that the sum of internal angles is equal to (n - 2) * 180, where n is the number of sides/angles in a polygon
# For further explanation I looked at this link "https://www.mathsisfun.com/geometry/interior-angles-polygons.html"
# So for a regular polygon, I just divided by n to find out the angle of rotation for each iteration, giving the final formula angle = ((n - 2) *  180) / n

num_angles = 3
max_num_angles = 10

tim.pensize(5)


for n in range(num_angles, max_num_angles + 1):  # range is 3-10 Inclusive
    angle = ((n - 2) * 180) / n
    r = random.random()
    g = random.random()
    b = random.random()
    tim.color((r, g, b))
    for _ in range(n):
        tim.forward(100)
        tim.right(180 - angle)

s = t.Screen()
s.exitonclick()
