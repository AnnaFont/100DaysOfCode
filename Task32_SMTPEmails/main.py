import pandas
import smtplib
import datetime as dt
import random


def send_email():
    # Send an email from your gmail. Check gmail settings first
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="testemail@yahoo.com",
                            msg=f"Subject:Happy Birthday\n\n{letter_text}")
        connection.close()


now = dt.datetime.now()

my_email = "testemail@gmail.com"
password = "abc123"

# Take the words from the csv
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today is the birthday of someone
if (now.month, now.day) in birthday_dict:
    # Choose a random letter
    letter_num = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_num}.txt") as letter_file:
        letter_text = letter_file.read()
        # Replace the text for the name of the birthday person
        letter_text = letter_text.replace("[NAME]", birthday_dict[(now.month, now.day)]["name"])
    send_email()

