from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake = []
        self.size = 3
        self.create_snake()

    def create_snake(self):
        colour = ('red', 'green', 'blue')
        for i in range(self.size):
            turtle = Turtle(shape='square')
            turtle.penup()
            # turtle.color(colour[i])
            turtle.color('white')
            turtle.goto(x=-(20 * i), y=0)
            self.snake.append(turtle)

    def move(self, heading):
        for index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)

        self.snake[0].setheading(heading)
        self.snake[0].forward(10)

    def can_move(self):
        timmy = self.snake[0]

        if 380.0 < timmy.xcor() or -380.0 > timmy.xcor() or 280.0 < timmy.ycor() or -280.0 > timmy.ycor():
            return False
        else:
            return True

    def move_arrow(self, heading):
        def bind_event():
            self.move(heading)
        return bind_event
