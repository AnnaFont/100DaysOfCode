from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Self to create a new property of the class
        self.window = Tk()
        self.score = 0
        self.window.title("Trivia Quizz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Set up score as label
        self.score_label = Label(text="Score: 0", font=("Arial", 13), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Canvas to add an image
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="Some question text", fill=THEME_COLOR,
            font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # To add the image it needs a specific type
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        # Set the buttons
        self.button_false = Button(image=false_img, highlightthickness=0, command=self.button_false_clicked)
        self.button_false.grid(column=1, row=2)

        self.button_true = Button(image=true_img, highlightthickness=0, command=self.button_true_clicked)
        self.button_true.grid(column=0, row=2)
        self.get_next_question()

        self.window.mainloop()

    # Fetch the text from the question brain and print it in the screen
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")



    def button_false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def button_true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question())
