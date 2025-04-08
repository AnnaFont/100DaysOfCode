import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "New_API"
TWILIO_SID =""
TWILIO_AUTH_TOKEN =""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
api_key = os.environ.get("NMAR6FCP3AVF9YEO")
# Include Twilio data here
account_sid = "TWILIO_ACCOUNT_ID"
auth_token = os.environ.get("AUTH_TOKEN")


param_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key,
}

# Retrieve data of the stock

response = requests.get(STOCK_ENDPOINT, params=param_stock)
# Use json viewer to check the structure
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

stock_price_dif = abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
print(stock_price_dif)

stock_dif_perc = round(stock_price_dif / float(yesterday_closing_price) * 100)

if stock_dif_perc < 4:
    # Send message
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTittle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=param_stock)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)
    # Single quote to do not confuse the code
    formatted_articles = [
        f"Headline: {article['title']}. \nBrief: {article['description']}" for
        article in three_articles]

    # Send it by sms using twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+15648393939",
            to="+15339293832"
        )