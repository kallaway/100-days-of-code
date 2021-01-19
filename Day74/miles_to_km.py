from tkinter import *


def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

input = Entry(width=5)
input.grid(column=1, row=0)

# Label

my_label = Label(text="Miles", font=("Arial", 18))
my_label.config(text="Miles")
my_label.grid(column=2, row=0)

new_label = Label(text="is equal to", font=("Arial", 18))
new_label.config(text="is equal to")
new_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

last_label = Label(text="Km", font=("Arial", 18))
last_label.config(text="Km")
last_label.grid(column=2, row=1)

# Button


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
