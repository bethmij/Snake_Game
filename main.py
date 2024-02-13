import time
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(900, 700)
screen.title('My Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.move_upwards, "Up")
screen.onkey(snake.move_downwards, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.05)

    is_move = snake.can_move()

    if is_move:
        snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
