# We will be creating a game of Snake.
# The seven steps that it takes to create the game:
# 1. Create the snake body
# 2. Move the snake
# 3. Create the food
# 4. Detect collision with food
# 5. Create the scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

import time
from turtle import Screen

from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

screen.exitonclick()
