from datetime import datetime
import os
import requests

APP_ID = "ec525137"
APP_KEY = "3742baa9b4ed0dcaee78163dc65be36a"
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/afont11/Workout_Anna/workouts"

GENDER = "Female"
WEIGHT_KG = 55
HEIGHT_CM = 169
AGE = 30


headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

# Ask the user what to log
user_in = input("Tell me what exercise did you do:")

# JSON data to the query
exercise_data = {
    "query": user_in,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


# Send the data to the API
response = requests.post(url=NUTRITIONIX_URL, json=exercise_data, headers=headers)

exercise_data = response.json()["exercise"]

print(exercise_data)

# Sheety headers
headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

# Loop each activity that the user input
for exercise in exercise_data:
    sheet_data = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    # Write the response in the Google sheets
    response = requests.post(url=SHEETY_URL, json=sheet_data, headers=headers)
    print(response.text)
