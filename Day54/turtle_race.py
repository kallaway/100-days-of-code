from turtle import Turtle, Screen
import random

has_race_started = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter a color. ")
colors = ["red", "blue", "orange", "green", "purple", "brown"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    has_race_started = True

while has_race_started:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            has_race_started = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, you lost. The {winning_color} turtle was the winner!")

        random_move = random.randint(0, 10)
        turtle.forward(random_move)

screen.exitonclick()