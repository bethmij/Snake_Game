from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVING_DISTANCE = 10
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        self.size = 3
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        # colour = ('red', 'green', 'blue')
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        turtle = Turtle(shape='square')
        turtle.penup()
        # turtle.color(colour[i])
        turtle.color('white')
        turtle.goto(position)
        self.snake.append(turtle)

    def move(self):
        for index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)

        self.head.forward(MOVING_DISTANCE)

    def can_move(self):
        timmy = self.snake[0]

        if 420.0 < timmy.xcor() or -430.0 > timmy.xcor() or 330.0 < timmy.ycor() or -320.0 > timmy.ycor():
            return False
        else:
            return True

    def move_upwards(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_downwards(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow_snake(self):
        self.add_snake(self.snake[-1].position())
