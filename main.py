import time
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(900, 700)
screen.title('My Snake Game')
screen.bgcolor('black')
screen.tracer(0)
snake = []
is_move = True
size = 3

colour = ('red', 'green', 'blue')

for i in range(size):
    turtle = Turtle(shape='square')
    turtle.penup()
    # turtle.color(colour[i])
    turtle.color('white')
    turtle.goto(x=-(20 * i), y=0)
    snake.append(turtle)


while is_move:
    screen.update()
    time.sleep(0.05)
    if 380.0 < turtle.xcor() or -380.0 > turtle.xcor() or 280.0 < turtle.ycor() or -280.0 > turtle.ycor():
        is_move = False

    for index in range(len(snake) - 1, 0, -1):
        new_x = snake[index - 1].xcor()
        new_y = snake[index - 1].ycor()
        snake[index].goto(new_x, new_y)

    snake[0].setheading(90)
    snake[0].forward(10)


screen.listen()
screen.onkey(move_snake(90), 'Up')
screen.onkey(move_snake(270), 'Down')
screen.onkey(move_snake(180), 'Left')
screen.onkey(move_snake(0), 'Right')
screen.exitonclick()
