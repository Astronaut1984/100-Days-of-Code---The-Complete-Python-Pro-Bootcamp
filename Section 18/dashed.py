import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for _ in range(10):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)

tim.hideturtle()

s = t.Screen()
s.exitonclick()