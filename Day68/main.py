import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_capitals = data.capital.to_list()
guessed_capitals = []

while len(guessed_capitals) < 50:
    answer_capital = screen.textinput(title=f"{len(guessed_capitals)}/50 Capitals Correct",
                                      prompt="What's another state's capital?").title()
    if answer_capital == "Exit":
        missing_states = [state for state in all_capitals if state not in guessed_capitals]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_capital in all_capitals:
        guessed_capitals.append(answer_capital)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        capitals_data = data[data.capital == answer_capital]
        t.goto(int(capitals_data.x), int(capitals_data.y))
        t.write(answer_capital)
