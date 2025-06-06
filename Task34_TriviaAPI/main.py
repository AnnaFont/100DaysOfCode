from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

parameters = {
    "amount": 10,
    "type": "boolean"
}

question_data = {}


def obtain_data():
    global question_data
    # Look for trivia questions
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]


question_bank = []
#obtain_data()
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# It cannot have two main loops. Tk main loop will be used, other is commented
# while quiz.still_has_questions():
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
