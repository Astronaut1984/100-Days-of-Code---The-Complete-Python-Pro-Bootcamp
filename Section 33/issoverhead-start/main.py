import requests
from datetime import datetime
import time

MY_LAT = 30.045980  # Your latitude
MY_LONG = 31.224312  # Your longitude

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # Your position is within +5 or -5 degrees of the ISS position.
    # If the ISS is close to my current position
    # and it is currently dark
    def met_requirements():
        return (
            abs(iss_latitude - MY_LAT) <= 5
            and abs(iss_longitude - MY_LONG) <= 5
            and (time_now >= sunset or time_now <= sunrise)
        )

    print(met_requirements())
    time.sleep(1)
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
