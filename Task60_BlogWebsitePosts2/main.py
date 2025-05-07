from flask import Flask, render_template, request
import requests
import smtplib

OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"


def send_email(data):
    email_content = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage:{data['message']}"
    # Send an email from your gmail. Check gmail settings first
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL, to_addrs=OWN_PASSWORD,
                            msg=f"Subject:New inquiry from website {data['name']}\n\n{email_content}")
        connection.close()


app = Flask(__name__)


blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
blog_response = response.json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=blog_response)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_email(data)
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")


@app.route("/form-entry")
def receive_data(data_contact):
    print(data_contact)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in blog_response:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
