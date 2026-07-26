##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import datetime as dt
from dotenv import dotenv_values
import random
import os

config = dotenv_values(".env")

FROM_EMAIL = config["FROM_EMAIL"]
PASSWORD = config["APP_PASS"]

# 1. Update the birthdays.csv
frame = pd.read_csv("birthdays.csv")
people = frame.to_dict(orient="records")
today = dt.datetime.now()

# 2. Check if today matches a birthday in the birthdays.csv
birthday_is_today = frame.loc[
    (frame["month"] == today.month) & (frame["day"] == today.day)
]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for name, email in zip(birthday_is_today["name"], birthday_is_today["email"]):
    file_path = os.path.join(
        "./letter_templates", random.choice(os.listdir(path="./letter_templates"))
    )
    letter = ""
    with open(file_path, "r") as f:
        letter = f.read().replace("[NAME]", name)

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        print(f"Sending Message to {name}...")
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{letter}",
        )