import random
import turtle as t
from turtle import Screen

pancho = t.Turtle()
pancho.shape("turtle")
pancho.speed("fastest")
pancho.pensize(3)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        pancho.color(random_color())
        pancho.circle(150)
        pancho.setheading(pancho.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
