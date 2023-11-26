from turtle import Turtle, Screen

pancho = Turtle()
pancho.shape("turtle")
pancho.color("DarkSeaGreen4")

for _ in range(4):
    pancho.forward(10)
    pancho.penup()
    pancho.forward(10)
    pancho.pendown()
    pancho.forward(10)
    pancho.penup()
    pancho.forward(10)
    pancho.pendown()
    pancho.forward(10)
    pancho.penup()
    pancho.forward(10)
    pancho.pendown()
    pancho.forward(10)
    pancho.penup()
    pancho.forward(10)
    pancho.pendown()
    pancho.right(90)

screen = Screen()
screen.exitonclick()
