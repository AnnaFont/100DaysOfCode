from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def button_reset_clicked():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def button_start_clicked():
    global reps
    # When count down finishes call function and increase reps
    reps += 1

    work_sec = WORK_MIN # * 60
    short_break_sec = SHORT_BREAK_MIN #* 60
    long_break_sec = LONG_BREAK_MIN #* 60

    # Some repetitions are long and some short
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        timer_label.config(text="WORK TIME", fg=RED)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK TIME", fg=GREEN)
    else:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK TIME", fg=PINK)


# Count in seconds
def count_down(count):
    minutes_count = math.floor(count/60)
    seconds_count = count % 60
    # In python you can change the data type of a variable
    if seconds_count < 10:
        seconds_count = f"0{seconds_count}"
    if seconds_count == 0:
        seconds_count = "00"
    # To change an item of canvas
    canvas.itemconfig(timer_text, text=f"{minutes_count}:{seconds_count}")

    # to do not continue to negative
    if count > 0:
        global timer
        # Takes the amount of time it has to pass to check something
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        button_start_clicked()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="YELLOW")


# Canvas to add an image, bg to change the background color, fg for foreground (highlightthickness to remove the square)
canvas = Canvas(width=200, height=224, bg="YELLOW", highlightthickness=0)
# To add the image it needs a specific type
tomato_img = PhotoImage(file="tomato.png")
# Add position and PhotoImage specified
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column= 2, row=2)


# Set up user interface
timer_label = Label(text="Timer", fg=GREEN, bg="YELLOW", font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=2, row = 1)

button_start = Button(text="Start", bg="YELLOW", command=button_start_clicked, highlightthickness=0)
button_start.grid(column=1, row=3)

button_reset = Button(text="Reset", bg="YELLOW", command=button_reset_clicked, highlightthickness=0)
button_reset.grid(column=3, row=3)

check_marks = Label(text="", fg=GREEN, bg="YELLOW")
check_marks.grid(column=2, row=3)

window.mainloop()
