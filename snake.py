from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.SNAKE = []
        # self.i = 0
        self.create_snake()
        self.head = self.SNAKE[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        body = Turtle()
        body.shape('square')
        body.color('white')
        body.penup()
        body.goto(position)
        self.SNAKE.append(body)

    def extend(self):
        """Add a new segment to the snake"""
        self.add_segment(self.SNAKE[-1].position())

    def reset_snake(self):
        for seg in self.SNAKE:
            seg.goto(1000, 1000)
        self.SNAKE.clear()
        self.create_snake()
        self.head = self.SNAKE[0]


    def move(self):
        for segment in range(len(self.SNAKE) - 1, 0, -1):
            new_x = self.SNAKE[segment - 1].xcor()
            new_y = self.SNAKE[segment - 1].ycor()
            self.SNAKE[segment].goto(new_x, new_y)
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