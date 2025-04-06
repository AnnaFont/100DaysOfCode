import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 1.2432
MY_LONG = -0.534
MY_EMAIL = "testemail@gmail.com"
MY_PASS = "abc123"

dict_param = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}


# Send email to check iss
def send_email():
    # Send an email from your gmail. Check gmail settings first
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:ISS notification\n\nHurry up, ISS is visible")
        connection.close()


# Execute the code every 60 seconds
while True:
    time.sleep(60)
    # Check iss location
    response = requests.get("https://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    iss_is_visible = False

    # Check current location is between +-5 deg of iss
    if abs(iss_lat - dict_param["lat"]) < 5 and abs(iss_long - dict_param["long"]) < 5:
        iss_is_visible = True

    response = requests.get("https://api.sunrise-sunset.org/json", params=dict_param)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    # Take the hour of the formatted sunrise
    hour_sunrise = int(sunrise.split("T")[1].split(":")[0])
    hour_sunset = int(sunset.split("T")[1].split(":")[0])

    # Get today hour
    time_now = datetime.now()

    is_dark_now = False
    # Compare if it is nighttime
    if time_now.hour < hour_sunrise or time_now.hour > hour_sunset:
        is_dark_now = True

    # Send and email if it is night and iss is visible
    if iss_is_visible and is_dark_now:
        send_email()
