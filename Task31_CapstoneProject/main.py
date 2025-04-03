from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# Take the words from the csv
data = pandas.read_csv("data/french_words.csv")
# Records it is used to sort it in a different way
words_dict = data.to_dict(orient="records")
current_card = {}


def next_card():
    # Change to a global to be used in other functions
    global current_card, flip_timer
    # Reset counter when the button is clicked
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Capstone Project")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas to add an image, bg to change the background color, fg for foreground
canvas = Canvas(width=800, height=526)
# To add the image it needs a specific type
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
# Add position and PhotoImage specified
canvas.create_image(400, 263, image=card_front_img)
card_background = canvas.create_image(400, 263, image=card_back_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()

