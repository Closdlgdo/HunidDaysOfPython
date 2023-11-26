from turtle import Turtle, Screen

pancho = Turtle()
pancho.shape("turtle")
pancho.color("DarkSeaGreen4")

for _ in range(3):
    pancho.forward(100)
    pancho.right(120)

for _ in range(4):
    pancho.forward(100)
    pancho.right(90)

for _ in range(5):
    pancho.forward(100)
    pancho.right(72)

for _ in range(6):
    pancho.forward(100)
    pancho.right(60)

for _ in range(7):
    pancho.forward(100)
    pancho.right(51.5)

for _ in range(8):
    pancho.forward(100)
    pancho.right(45)

for _ in range(9):
    pancho.forward(100)
    pancho.right(40)

for _ in range(10):
    pancho.forward(100)
    pancho.right(36)

screen = Screen()
screen.exitonclick()
