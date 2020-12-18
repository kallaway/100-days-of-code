import turtle as t
import random

tommy = t.Turtle()

colors = ["teal", "burlywood", "dark turquoise", "firebrick", "medium violet red", "pale violet red", "blue violet",
          "sea green"]
directions = [0, 90, 180, 270]
tommy.pensize(12)
tommy.speed("fastest")

for _ in range(200):
    tommy.color(random.choice(colors))
    tommy.forward(30)
    tommy.setheading(random.choice(directions))


