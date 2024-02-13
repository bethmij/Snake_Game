import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(700, 600)
screen.title('My Snake Game')
screen.bgcolor('black')
snake = []
is_move = True
size = 3


def move_forward():
    for snake_bloke in snake:
        snake_bloke.forward(10)


def move_backward():
    for snake_bloke in snake:
        snake_bloke.backward(10)


def move_upward():
    for snake_bloke in snake:
        snake_bloke.setheading(0)
        snake_bloke.forward(10)


def move_downward():
    for snake_bloke in snake:
        snake_bloke.setheading(270)
        snake_bloke.forward(10)


for i in range(size):
    turtle = Turtle(shape='square')
    turtle.penup()
    turtle.color('white')
    turtle.goto(x=20 * i, y=0)
    snake.append(turtle)

while is_move:

    if turtle.xcor() > 310.0:
        is_move = False

    screen.onkey(move_forward, 'up')
    screen.onkey(move_forward, 'up')
    screen.onkey(move_forward, 'up')
    screen.onkey(move_forward, 'up')
    move_snake()

screen.exitonclick()
