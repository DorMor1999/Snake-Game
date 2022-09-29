from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POS:
            self.add_part(position)

    def move(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[part].goto(self.snake_parts[part - 1].xcor(), self.snake_parts[part - 1].ycor())
        self.snake_parts[0].forward(move_distance)

    def extend(self):
        self.add_part(self.snake_parts[-1].position())

    def add_part(self, position):
        new_snake_part = Turtle(shape="square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.goto(position)
        self.snake_parts.append(new_snake_part)

    def up(self):
        if self.snake_parts[0].heading() != down:
            self.snake_parts[0].setheading(up)

    def down(self):
        if self.snake_parts[0].heading() != up:
            self.snake_parts[0].setheading(down)

    def left(self):
        if self.snake_parts[0].heading() != right:
            self.snake_parts[0].setheading(left)

    def right(self):
        if self.snake_parts[0].heading() != left:
            self.snake_parts[0].setheading(right)

    def reset(self):
        for part in self.snake_parts:
            part.goto(2000, 2000)
        self.snake_parts.clear()
        self.create_snake()
