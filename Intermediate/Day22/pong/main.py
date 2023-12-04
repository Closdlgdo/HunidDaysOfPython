# We will create a Pong game using Pygame.
# There are seven different steps that it takes to create the game:
# 1. Create the screen
# 2. Create the paddle
# 3. Move the paddle
# 4. Create the ball
# 5. Move the ball
# 6. Detect collision with wall
# 7. Detect collision with paddle

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


def move_up():
    y = paddle.ycor()
    y += 20
    paddle.sety(y)


def move_down():
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)
