
# from turtle import Turtle, Screen
#
# Timmy = Turtle()
# print(Timmy)
# Timmy.shape("turtle")
# Timmy.color("chartreuse4")
# Timmy.forward(100)
# Timmy.lt(90)
# Timmy.forward(100)
# Timmy.lt(90)
# Timmy.forward(100)
# Timmy.lt(90)
# Timmy.forward(100)
# # has attributes: Timmy.walk, Timmy.eat
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# # does methods: Timmy.move, Timmy.stop
#
# my_screen.exitonclick()

from prettytable import PrettyTable

Table = PrettyTable()
Table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
Table.add_column("Type", ["Electric", "Water", "Fire"])
Table.align = "l"
print(Table)

