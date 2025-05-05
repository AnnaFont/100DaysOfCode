# higher-lower game
from flask import Flask
import random

app = Flask(__name__)

# Main page
@app.route('/')
def init_page():
    # It can be added html and css in the response (Flask accept it)
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExemZyc3AwczRiZjAwbjFsOHljMjYyc3JydW9neHBjc' \
           'DJ3N2UwZnFlZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DhiRqIsofVMi7fWNBQ/giphy.gif" width = 600>'


# Generate a random number
rand_num = random.randint(0, 9)

# Check the website number and save it in the variable num_user
@app.route("/<int:num_user>")
def guess_number(num_user):
    # Check the guessed number
    if num_user == rand_num:
        return "<h1 style='color: green'>Correct! </h1>" \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width = 200>'
    elif num_user > rand_num:
        return "<h1 style='color: red'>Too high, try again!</h1>"  \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width = 200>'
    else:
        return "<h1 style='color: blue'>Too low, try again!</h1>" \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width = 200>'


if __name__ == "__main__":
    # Debug to true it allows to do not stop the code when changing the code, only saving will update the website
    app.run(debug=True)


