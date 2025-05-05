# Simple flask server
from flask import Flask
from flask import render_template
import random
import jinja2
import datetime
import requests
app = Flask(__name__)

# Main page
@app.route('/')
def home_page():
    rand_num = random.randint(0, 9)
    # It is going to take the information from the html file
    # The file must be in the templates folder and pictures in the static folder
    year_today = datetime.datetime.now().year
    return render_template("index.html", num=rand_num, year=year_today)


@app.route('/guess/<name_user>')
def name_page(name_user):
    gender_url = f"https://api.genderize.io?name={name_user}"
    gender_response = requests.get(gender_url).json()
    gender_user = gender_response["gender"]
    age_url = f"https://api.agify.io?name={name_user}"
    age_response = requests.get(age_url).json()
    age_user = age_response["age"]
    return render_template("guess.html", name=name_user, gender=gender_user, age=age_user)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/4b2ca8c3f4b81d802d92"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(all_posts)
    return render_template("blog.html", post=all_posts)


if __name__ == "__main__":
    # Debug to true it allows to do not stop the code when changing the code, only saving will update the website
    app.run(debug=True)
