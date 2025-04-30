# Web development
# Full Stack = Front End (HTML, CSS & JS) + Back-End (JS or Py)
# It can be use frameworks which has already some pre-build code

# Flask and Django are used in the backend as web development frameworks built in python
# Framework in difference with library is that the framework call your code not the way round

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def Hello_World():
    return 'Hey'

if __name__ == "__main__":
    app.run()

# TO RUN IT, IN TERMINAL LOCAL :
# export FLASK_APP=main.py
# flask run
# Click on http://127.0.0.1:5000
# Click CTRL+C when finish
# Else it can be used in the code (easier):
# if __name__ == "__main__":
#   app.run()

