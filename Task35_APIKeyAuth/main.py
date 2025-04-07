# API key must be created in some websites to access the data
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

MY_LAT = 32.0828
MY_LONG = -1.43

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWN_API_KEY")

# Include Twilio data here
account_sid = "TWILIO_ACCOUNT_ID"
auth_token = os.environ.get("AUTH_TOKEN")

location_dict = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

# Retrieve data of the weather
response = requests.get("https://api.openweathermap.org", params=location_dict)
response.raise_for_status()
data = response.json()

weather = data["list"][0]["weather"][0]["id"]
it_will_rain = False

# Loop through the hours to check the weather
for hour in data["list"]:
    rain_24hours = int(hour["weather"][0]["id"])
    # Code, lower than 700, it rains
    if rain_24hours < 700:
        it_will_rain = True

# Bring an umbrella if the probability of rain is high
if it_will_rain:
    print("Bring an umbrella")
    # Twilio can send SMS, email, voice (10 hours for free only)
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an ☔️", from_="YOUR TWILIO VIRTUAL NUMBER",
                to="YOUR TWILIO VERIFIED REAL NUMBER")
    # To send whatsapp messages https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn

