from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="New Button")
button.grid(column=2, row=0)

# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
