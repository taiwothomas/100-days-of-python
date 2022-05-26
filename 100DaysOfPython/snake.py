from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
L = 280.00


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        x = 0
        y = 0
        for thing in range(3):
            self.add_segment(x, y)
            x -= 20

    def add_segment(self, x, y):
        snake_v = Turtle()
        snake_v.shape("square")
        snake_v.color("white")
        snake_v.penup()
        snake_v.goto(x, y)
        self.snake.append(snake_v)

    def grow(self):
        self.add_segment(self.snake[-1].xcor(), self.snake[-1].ycor())

    def move(self):
        for v in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[v - 1].xcor()
            new_y = self.snake[v - 1].ycor()
            self.snake[v].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def switch_side(self):
        if self.head.xcor() > L:
            self.head.setx(-L)
        elif self.head.xcor() < -L:
            self.head.setx(L)

        if self.head.ycor() > L:
            self.head.sety(-L)
        elif self.head.ycor() < -L:
            self.head.sety(L)
