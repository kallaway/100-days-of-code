from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/spanish_words.csv")
need_to_learn = data.to_dict(orient="records")
current_card = {}


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(need_to_learn)
    canvas.itemconfig(card_title, text="Spanish")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ***********************************  UI SETUP ************************************
window = Tk()
window.title("Spanish Translator")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=new_card)
right_button.grid(row=1, column=1)

# ************************** CREATE FLASH CARDS **********************
new_card()

window.mainloop()
