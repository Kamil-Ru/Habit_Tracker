import requests
from config import *
from datetime import datetime

neutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

HEADERS = {
    "x-app-id": APP_ID_NUTRI,
    "x-app-key": API_KEY_NUTRI,
    "x-remote-user-id": "0",
}

config = {
     "query": input("Type your exercise: "),
     "gender": "male",
     "weight_kg": 72,
     "height_cm": 183,
     "age": 30
}

response = requests.request("POST", url=neutri_endpoint, headers=HEADERS, data=config)
response_data = response.json()
response_data_exercises = response_data["exercises"]

for _ in range(len(response_data_exercises)):
    exercise_type = response_data_exercises[_]["name"]
    duration = response_data_exercises[_]["duration_min"]
    calories = response_data_exercises[_]["nf_calories"]


    data_now = datetime.now()
    data = data_now.strftime("%d/%m/%Y")
    time = data_now.strftime("%H:%M:%S")

    url_sheety = URL_SHEETY

    headersAuth = {
        'Authorization': f'Bearer {BEARER_AUTHENTICATION}'
    }
    body = {
        "workout": {
            "date": data,
            "time": time,
            "exercise": exercise_type.title(),
            "duration": duration,
            "calories": calories
        }
    }
    response = requests.post(url=url_sheety, json=body, headers=headersAuth)

