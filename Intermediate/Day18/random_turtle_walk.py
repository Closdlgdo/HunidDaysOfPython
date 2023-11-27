import random
import turtle as t

pancho = t.Turtle()
pancho.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
pancho.pensize(10)
pancho.speed("fastest")

for _ in range(200):
    pancho.color(random_color())
    pancho.forward(30)
    pancho.setheading(random.choice(directions))
