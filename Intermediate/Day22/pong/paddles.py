# This is the paddle class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)

    def move_up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def move_down(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)
