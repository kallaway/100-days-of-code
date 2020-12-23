from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()