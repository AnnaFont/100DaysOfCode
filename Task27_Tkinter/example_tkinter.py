from tkinter import *


def button_clicked():
    # To change the text of a label
    new_text = input_box.get()
    new_label.config(text=f"Button clicked -Text {new_text}")


window = Tk()
window.title("GUI program")
window.minsize(500, 300)
# Leave a bit of space of the grid
window.config(padx=20, pady=20)

# Create a label (L in mayus)
new_label = Label(text="I am a label", font=("Arial", 13, "bold"))
new_label.config(text="New text")
# It is needed to show the label in the screen. It is used to layout the items in the screen
# new_label.pack(side="left")
new_label.grid(column=3, row=3)

# Create buttons
button = Button(text="click me", command=button_clicked)
# Grid is used as pack but like in rows and columns
button.grid(column=2, row=2)

# Entry - Add a box to enter some text
input_box = Entry(width=15)
print(input_box.get())
# Place is like pack but you can be more specific
# input_box.place(x=0, y=0)
input_box.grid(column=1, row=1)


# Unlimited arguments. * means that it can be added unlimited arguments
def add(*args):
    out = 0
    for n in args:
        out += n
    return out


# Unlimited keyword argument ** kwargs
def calculate(**kwargs):
    print(kwargs["add"])
    # Using get does the same but if the keyword is not defined it will return none
    print(kwargs.get("add"))


calculate(add=3, multiply=5)

# Keep the window in the screen - write at the end of the program
window.mainloop()
