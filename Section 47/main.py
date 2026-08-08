import requests
from bs4 import BeautifulSoup
import smtplib
import dotenv

CONFIG = dotenv.dotenv_values(".env")
URL = "https://appbrewery.github.io/instant_pot/"
THRESHOLD = 100

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

try:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
except Exception as err:
    print(f"Error getting website: {err}")
    exit()

content = response.text

soup = BeautifulSoup(content, "html.parser")

price = soup.select_one(".a-offscreen").getText()
price = price.split("$")[1]
price_float = float(price)

product_title_raw = soup.select_one("#productTitle").getText()
product_title = " ".join(product_title_raw.split())

message = f"{product_title} is now ${price_float}\n{URL}"

if price_float < THRESHOLD:
    server = smtplib.SMTP(host=CONFIG["SMTP_ADDRESS"], port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(user=CONFIG["EMAIL_ADDRESS"], password=CONFIG["EMAIL_PASSWORD"])

    server.sendmail(
        from_addr=CONFIG["EMAIL_ADDRESS"],
        to_addrs=CONFIG["TO_ADDRESS"],
        msg=f"Subject: Amazon Price Alert!\n\n{message}".encode("utf-8"),
    )
