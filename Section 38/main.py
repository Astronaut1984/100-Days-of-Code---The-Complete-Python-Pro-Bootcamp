import requests, json, datetime as dt
from dotenv import dotenv_values

config = dotenv_values(".env")


API_KEY = config["API_KEY"]
APP_ID = config["APP_ID"]
nutrition_headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
NUTRITION_URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

nutrition_body = json.loads(config["HEALTH_DATA"])
query = input("Tell me which exercise you did: ")
nutrition_body["query"] = query

result = requests.post(
    url=NUTRITION_URL,
    json=nutrition_body,
    headers=nutrition_headers,
)

result.raise_for_status()
result = result.json()["exercises"][0]
print(result)

SHEETY_URL = config["SHEETY_URL"]
SHEETY_BEARER = config["SHEETY_BEARER"]
# duration_min, nf_calories, name
curr_date = dt.datetime.now().strftime("%d/%m/%Y")
curr_time = dt.datetime.now().strftime("%X")
sheety_body = {
    "workout": {
        "date": curr_date,
        "time": curr_time,
        "exercise": result["name"].title(),
        "duration": result["duration_min"],
        "calories": result["nf_calories"],
    }
}

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER}",
    "Content-Type": "application/json",
}

sheety_result = requests.post(url=SHEETY_URL, json=sheety_body, headers=sheety_headers)
sheety_result.raise_for_status()

print(sheety_result.text)
