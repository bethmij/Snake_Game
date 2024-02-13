import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(700, 600)
screen.title('My Snake Game')
screen.bgcolor('black')
snake = []
is_move = True
size = 3


def move_snake(heading: int):
    def inner_function():
        for index, snake_bloke in enumerate(snake[::-1]):

            xcor = snake_bloke.xcor() if index == 2 else 0

            if snake_bloke.xcor() == xcor:
                snake_bloke.speed('fastest')
                snake_bloke.setheading(heading)

            snake_bloke.forward(10)

    return inner_function



for i in range(size):
    turtle = Turtle(shape='square')
    turtle.penup()
    turtle.color('white')
    turtle.goto(x=-(20 * i), y=0)
    snake.append(turtle)
# snake.reverse()

while is_move:
    if 310.0 < turtle.xcor() or -280.0 > turtle.xcor() and 280.0 < turtle.ycor() or -280.0 > turtle.ycor():
        is_move = False

    move_snake(90)



# screen.listen()
# screen.onkey(move_snake(90), 'Up')
# screen.onkey(move_snake(270), 'Down')
# screen.onkey(move_snake(0), 'Left')
# screen.onkey(move_snake(180), 'Right')
screen.exitonclick()
