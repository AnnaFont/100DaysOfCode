from tkinter import *
# Module of code is not imported - it is used for pop ups
from tkinter import messagebox
import random
# Useful to copy and paste
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def button_genpass_clicked():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    pass_entry.delete(0, END)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    # It copies the password automatically
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def button_add_clicked():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    fills_empty = False

    if len(website) == 0 or len(password) == 0:
        fills_empty = True
        messagebox.showinfo(title="Error", message=f"Fields cannot be empty")
    if not fills_empty:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details enter: \nEmail: {email}"
                                                          f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

            # To delete the entrance from the start until the end
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "@gmail.com")
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas to add an image, bg to change the background color, fg for foreground
canvas = Canvas(width=200, height=200)
# To add the image it needs a specific type
logo_img = PhotoImage(file="logo.png")
# Add position and PhotoImage specified
canvas.create_image(100, 100, image=logo_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=2, row=1)

# Set up user interface - Labels
website_label = Label(text="Website:", width=20)
website_label.grid(column=1, row=2)

email_label = Label(text="Email/Username:", width=20)
email_label.grid(column=1, row=3)

pass_label = Label(text="Password:", width=20)
pass_label.grid(column=1, row=4)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=2, row=2, columnspan=3)
# Put the cursor in the first entrance
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=2, row=3, columnspan=3)
email_entry.insert(0, "@gmail.com")

pass_entry = Entry(width=35)
pass_entry.grid(column=2, row=4, columnspan=2)

# Column span to add more than one column
button_genpass = Button(text="Generate Pass", width=10, command=button_genpass_clicked)
button_genpass.grid(column=3, row=4)

button_add = Button(text="Add", width=36, command=button_add_clicked)
button_add.grid(column=2, row=5, columnspan=3)

window.mainloop()
