from turtle import Turtle, Screen

pancho = Turtle()
pancho.shape("turtle")
pancho.color("DarkSeaGreen4")

for i in range(4):
    pancho.forward(100)
    pancho.right(90)

screen = Screen()
screen.exitonclick()
