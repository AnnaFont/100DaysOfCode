# Web development
from flask import Flask

app = Flask(__name__)

# Main page
@app.route('/')
def Hello_World():
    # It can be added html and css in the response (Flask accept it)
    return '<h1 style="text-align: center">Hey</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGE1ODN0MmZwb3NnYmxkMHd4N2J5MTVveDM4YWpobHd' \
           'zajQ3YjZraCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DgaabECbM9gc0/giphy.gif" width = 200>'


# Specific subpage
@app.route('/username/<name>')
def Hello_specific(name):
    return f"Hey {name}"


if __name__ == "__main__":
    # Debug to true it allows to do not stop the code when changing the code, only saving will update the website
    app.run(debug=True)


