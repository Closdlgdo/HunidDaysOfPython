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
screen.setup(width=700, height=400)
user_bet = screen.textinput(title="They call me Rabbit, This is a Turtle Race",
                            prompt="(Racers: luis, juan, pedro, pancho) Enter your choice: ")
print(user_bet)

turtles = {
    "pancho": Turtle(shape="turtle"),
    "pedro": Turtle(shape="turtle"),
    "juan": Turtle(shape="turtle"),
    "luis": Turtle(shape="turtle")
}

# Set colors using the Turtle.color() method
turtles["pancho"].color("blue")
turtles["pedro"].color("green")
turtles["juan"].color("red")
turtles["luis"].color("orange")

# Adjust the y-coordinates of each turtle
start_y = -100
for turtle_name, turtle in turtles.items():
    turtle.penup()
    turtle.goto(x=-330, y=start_y)
    start_y += 50  # Increase the separation along the y-axis

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_name, turtle in turtles.items():
        if turtle.xcor() > 330:
            is_race_on = False
            winning_turtle_name = turtle_name
            if winning_turtle_name == user_bet:
                print(f"You've won! {winning_turtle_name} is the winner!")
            else:
                print(f"You've lost! {winning_turtle_name} is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
