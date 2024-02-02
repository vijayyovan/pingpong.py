from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(40)
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1



    # ball = turtle.Turtle()
    # ball.speed(40)
    # ball.shape("circle")
    # ball.color("blue")
    # ball.penup()
    # ball.goto(0, 0)
    # ball.dx = 5
    # ball.dy = -5
