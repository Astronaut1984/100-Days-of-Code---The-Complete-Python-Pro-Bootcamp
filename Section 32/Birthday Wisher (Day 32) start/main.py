import smtplib
import dotenv
import datetime as dt
from pprint import pprint
import random as rnd

# Get quotes
quotes = []
with open("quotes.txt", "r") as f:
    quotes = [quote for quote in f]

quote = rnd.choice(quotes)
print(quote)

curr_day = dt.datetime.now().weekday()

if curr_day == 5:
    config = dotenv.dotenv_values(".env")

    from_email = config["FROM_EMAIL"]
    to_email = config["TO_EMAIL"]
    password = config["APP_PASS"]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        print("Sending Message...")
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:Motivational\n\n{quote}",
        )