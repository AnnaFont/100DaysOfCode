import smtplib
import datetime as dt
import random

now = dt.datetime.now()

my_email = "testemail@gmail.com"
password = "abc123"

# Check that it is Monday
if now.weekday() == 0:

    # Check in quotes file a random sentence
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # Send an email from your gmail. Check gmail settings first
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="testemail@yahoo.com",
                        msg=f"Subject:Hello\n\nThis is the body of the email:\n{quote}")
        connection.close()


# Create a datetime object
# date_of_birth = dt.datetime(year=1993, month=9, day=13)
