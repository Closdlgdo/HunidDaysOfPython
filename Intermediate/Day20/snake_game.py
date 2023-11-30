# We will be creating a game of Snake.
# The seven steps that it takes to create the game:
# 1. Create the snake body
# 2. Move the snake
# 3. Create the food
# 4. Detect collision with food
# 5. Create the scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Create the snake body. Each turtle is 20x20 pixels.
segment_1 = Turtle("square")
segment_1.color("white")

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-20, 0)

segment_3 = Turtle("square")
segment_3.color("white")
segment_3.goto(-40, 0)

screen.exitonclick()
