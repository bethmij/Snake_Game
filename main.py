import time
from turtle import  Screen
from snake import Snake

screen = Screen()
screen.setup(900, 700)
screen.title('My Snake Game')
screen.bgcolor('black')
screen.tracer(0)

is_move = True


snake = Snake()
screen.update()

while is_move:
    screen.update()
    time.sleep(0.05)

    is_move = snake.can_move()

    if is_move:
        snake.move(0)


screen.listen()
screen.onkey(snake.(90), 'Up')
screen.onkey(move_snake(270), 'Down')
screen.onkey(move_snake(180), 'Left')
screen.onkey(move_snake(0), 'Right')
screen.exitonclick()
