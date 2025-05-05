# Simple flask server
from flask import Flask
from flask import render_template

app = Flask(__name__)

# Main page
@app.route('/')
def home_page():
    # It is going to take the information from the html file
    # The file must be in the templates folder and pictures in the static folder
    return render_template("index.html")


if __name__ == "__main__":
    # Debug to true it allows to do not stop the code when changing the code, only saving will update the website
    app.run(debug=True)
