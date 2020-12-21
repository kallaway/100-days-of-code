from turtle import Turtle, Screen

Evan = Turtle()

screen = Screen()


def move_forwards():
    Evan.forward(10)


def move_backwards():
    Evan.backward(10)


def turn_left():
    new_heading = Evan.heading() + 10
    Evan.setheading(new_heading)


def turn_right():
    Evan.right(10)


def clear():
    Evan.clear()
    Evan.penup()
    Evan.home()
    Evan.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
