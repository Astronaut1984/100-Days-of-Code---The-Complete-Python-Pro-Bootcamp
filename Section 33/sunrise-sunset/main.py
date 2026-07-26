import requests

LAT = 30.044420
LNG = 31.235712

params = {"lat": LAT, "lng": LNG, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/v2", params=params)
response.raise_for_status()

data = response.json()

sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
