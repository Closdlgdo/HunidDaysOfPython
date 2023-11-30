# Object = pancho while the class = Turtle()
# We can have many classes of "Turtle()" with differently named Objects. For Example:
# Object = pedro, class = Turtle(); Object = luis, class = Turtle(); Object = juan, class = Turtle().
# Each object has its own state and is an instance of the class.
# We will create a class with 4 objects: pedro, luis, juan and pancho. Each object will have its own state.
# They will be assigned some sort of randomness so that they can race each other.
# We will also create a pop-up that asks the user to pick a name as selection of who they think will win the race.
# As soon as the turtle crosses the finish line, it will print out saying if we won or lost.

import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="They call me Rabbit, This is a Turtle Race",
                            prompt="(Racers: luis, juan, pedro, pancho) Enter your choice: ")
print(user_bet)
turtle_racers = {"luis": "orange", "juan": "red", "pedro": "green", "pancho": "blue"}

pancho = Turtle(shape="turtle")
pancho.penup()
pancho.color("blue")
pancho.goto(x=-240, y=-100)

pedro = Turtle(shape="turtle")
pedro.penup()
pedro.color("green")
pedro.goto(x=-240, y=-25)

juan = Turtle(shape="turtle")
juan.penup()
juan.color("red")
juan.goto(x=-240, y=50)

luis = Turtle(shape="turtle")
luis.penup()
luis.color("orange")
luis.goto(x=-240, y=125)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in (pancho, pedro, juan, luis):
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle_racers
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
