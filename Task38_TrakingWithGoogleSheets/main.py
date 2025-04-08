import requests

APP_ID = "ec525137"
APP_KEY = "3742baa9b4ed0dcaee78163dc65be36a"
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

# Ask the user what to log
user_in = input("Tell me what exercise did you do:")

# JSON data to the query
exercise_data = {
    "query": user_in
}

# Send the data to the API
response = requests.post(url=NUTRITIONIX_URL, json=exercise_data, headers=headers)

print(response.text)
# Write in the google sheets