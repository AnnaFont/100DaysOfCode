from tkinter import *


def button_clicked():
    # To change the text of a label
    km_calculation = int(input_miles.get()) * 1.60934
    input_km.config(text=str(km_calculation))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(400, 100)
# Leave a bit of space of the grid in pixels
window.config(padx=20, pady=20)

# Add text of miles, km and is equal to
Label(text="Miles", font=("Arial", 13)).grid(column=3, row=1)
Label(text="is equal to", font=("Arial", 13)).grid(column=1, row=2)
Label(text="Km", font=("Arial", 13)).grid(column=3, row=2)

# Create input entry of miles
input_miles = Entry(width=15)
print(input_miles.get())
input_miles.grid(column=2, row=1)

# Create input label of km
input_km = Label(text="0")
input_km.grid(column=2, row=2)

# Create button to calculate the miles to km
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

# Keep the window in the screen - write at the end of the program
window.mainloop()
