from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

driver.maximize_window()

driver.implicitly_wait(5)

if driver.find_elements(By.ID, value="langSelect-EN"):
    lang_button = driver.find_element(By.ID, value="langSelect-EN")
    print(lang_button)
    lang_button.click()

if driver.find_elements(By.LINK_TEXT, value="Got it!"):
    dismiss = driver.find_element(By.LINK_TEXT, value="Got it!")
    dismiss.click()


def get_highest_product():
    products_list = driver.find_elements(By.CSS_SELECTOR, value="#products > .product")
    prices_list = driver.find_elements(
        By.CSS_SELECTOR, value="#products > .product .price"
    )
    prices_list = [price.text.replace(",", "") for price in prices_list]
    print(prices_list)
    max_price = int(prices_list[0])
    cookies = driver.find_element(By.ID, value="cookies").text
    cookies_val = int(cookies.split(" ")[0])
    for price in prices_list[1:]:
        try:
            if int(price) < int(cookies_val) and int(price) > int(max_price):
                max_price = price
        except ValueError:
            continue
    idx = prices_list.index(str(max_price))
    products_list[idx].click()


cookie = driver.find_element(By.ID, value="bigCookie")

while True:
    timeout = 5
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        cookie.click()
    get_highest_product()
