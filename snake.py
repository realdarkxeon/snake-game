import turtle
VELOCITY = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, size):
        self.body = []
        for i in range(size):
            self.add((-VELOCITY * i, 0))
        self.head = self.body[0]

    def add(self, pos):
        block = turtle.Turtle("circle")
        block.penup()
        block.goto(pos)
        block.color("green")
        self.body.append(block)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto((self.body[i - 1].xcor(), self.body[i - 1].ycor()))
        self.head.forward(VELOCITY)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self, size):
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body.clear()
        for i in range(size):
            self.add((-VELOCITY * i, 0))
        self.head = self.body[0]
