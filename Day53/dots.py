import turtle as turtle_module
import random

turtle_module.colormode(255)
dotty = turtle_module.Turtle()
dotty.speed("fastest")
dotty.penup()
dotty.hideturtle()
color_list = [(180, 66, 21), (186, 14, 3), (215, 152, 98), (79, 38, 16), (229, 209, 186), (235, 163, 5), (246, 204, 0), (199, 3, 8), (235, 203, 98), (215, 79, 56)]

dotty.setheading(225)
dotty.forward(300)
dotty.setheading(0)
num_dots = 100

for dot_count in range(1, num_dots + 1):
    dotty.dot(20, random.choice(color_list))
    dotty.forward(50)

    if dot_count % 10 == 0:

        dotty.setheading(90)
        dotty.forward(50)
        dotty.setheading(180)
        dotty.forward(500)
        dotty.setheading(0)
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
screen = turtle_module.Screen()
screen.exitonclick()