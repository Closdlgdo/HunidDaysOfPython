import random
from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.pensize(7)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

for _ in range(200):
    t.color(random.choice(colors))
    t.forward(40)
    t.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
