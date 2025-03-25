class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # Check if questions left
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Pull a new question from the list
    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question} (True/False):")
        self.check_answer(user_answer, current_answer)

    def check_answer(self, user_answer, current_answer):
        if current_answer == user_answer:
            print("You got it right")
            self.score += 1
        else:
            print("Wrong answer")
        print(f"Correct answer is {current_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

