from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
segments = []

snake = Snake()
food = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_running = True
while is_game_running:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        board.increase_score()
        food.refresh()
        snake.extend()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        board.reset_scoreboard()
        snake.reset_snake()

    # Detect Collision with tail
    for segment in snake.SNAKE[1:]:
        if snake.head.distance(segment) < 10:
            board.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
