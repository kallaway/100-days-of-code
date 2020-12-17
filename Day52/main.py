from turtle import Turtle, Screen

tatiana = Turtle()
tatiana.shape("turtle")
tatiana.color("red")

# draw a square
# for _ in range(4):
#     tatiana.forward(100)
#     tatiana.right(90)

# draw a dashed line

for _ in range(15):
    tatiana.forward(10)
    tatiana.penup()
    tatiana.forward(10)
    tatiana.pendown()














screen = Screen()
screen.exitonclick()