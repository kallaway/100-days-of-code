import turtle as t
import random

tommy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tommy.pensize(12)
tommy.speed("fastest")

for _ in range(200):
    tommy.color(random_color())
    tommy.forward(30)
    tommy.setheading(random.choice(directions))
