import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player = None
        self.create_player()

    def create_player(self):
        self.player = turtle.Turtle()
        self.player.shape("turtle")
        self.player.color("black")
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)

    def go_up(self):
        self.player.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.player.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
