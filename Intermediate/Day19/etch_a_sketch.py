from turtle import Turtle, Screen

pancho = Turtle()
screen = Screen()


def move_forward():
    pancho.forward(15)


def move_backward():
    pancho.backward(15)


def turn_left():
    new_heading = pancho.heading() + 15
    pancho.setheading(new_heading)


def turn_right():
    new_heading = pancho.heading() - 15
    pancho.setheading(new_heading)


def make_bold():
    current_width = pancho.width()
    new_width = current_width + 3
    pancho.width(new_width)


def make_unbold():
    current_width = pancho.width()
    new_width = current_width - 3
    pancho.width(new_width)


def clear():
    pancho.clear()
    pancho.penup()
    pancho.home()
    pancho.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="b", fun=make_bold)
screen.onkey(key="x", fun=make_unbold)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
