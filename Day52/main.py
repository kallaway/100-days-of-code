from turtle import Turtle, Screen
import random

tatiana = Turtle()
tatiana.shape("turtle")

# draw a square
# for _ in range(4):
#     tatiana.forward(100)
#     tatiana.right(90)

# draw a dashed line

# for _ in range(15):
#     tatiana.forward(10)
#     tatiana.penup()
#     tatiana.forward(10)
#     tatiana.pendown()

colors = ["teal", "burlywood", "dark turquoise", "firebrick", "medium violet red", "pale violet red", "blue violet",
          "sea green"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tatiana.forward(100)
        tatiana.right(angle)


for shape_side_n in range(3, 11):
    tatiana.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
