import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXC
from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement
import time
import os

dotenv.load_dotenv()
TIMEOUT_INTERVAL = 2
PROMISED_DOWN = 30
PROMISED_UP = 30


class InternetSpeedYBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        # Initialize a driver instance
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=TIMEOUT_INTERVAL)

        self.up = 0
        self.down = 0

    def __wait_for_finish(self, max_wait, fn) -> WebElement:
        retries = max_wait // TIMEOUT_INTERVAL
        while True and retries:
            try:
                return self.wait.until(fn())
            except exceptions.TimeoutException:
                retries -= 1

        raise exceptions.TimeoutException(f"Condition not met after {max_wait} seconds")

    def get_internet_speed(self):
        self.driver.get(os.environ.get("SPEED_TEST_URL"))
        show_more_button = self.__wait_for_finish(
            60,
            lambda: EXC.element_to_be_clickable(
                (By.XPATH, '//*[@id="show-more-details-link"]')
            ),
        )
        download_speed = self.wait.until(
            EXC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#speed-value.succeeded")
            )
        )
        show_more_button.click()
        upload_speed = self.__wait_for_finish(
            60,
            lambda: EXC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#upload-value.succeeded")
            ),
        )
        self.up = int(upload_speed.text)
        self.down = int(download_speed.text)

    def __login(self):
        login_button = self.wait.until(
            EXC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/a[4]"))
        )
        login_button.click()

        email_text = self.wait.until(
            EXC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))
        )
        password_text = self.wait.until(
            EXC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))
        )

        email_text.clear()
        password_text.clear()

        email_text.send_keys(os.environ.get("Y_EMAIL"))
        password_text.send_keys(os.environ.get("Y_PASS"))

        login_button = self.wait.until(
            EXC.element_to_be_clickable((By.XPATH, "/html/body/div/div/form/button"))
        )
        login_button.click()

    def tweet_at_provider(self, message):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "t")
        self.driver.get(os.environ.get("Y_URL"))
        self.__login()

        post_button = self.wait.until(
            EXC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/button"))
        )
        post_button.click()

        post_content = self.wait.until(
            EXC.element_to_be_clickable((By.XPATH, '//*[@id="modal-compose"]'))
        )
        post_content.clear()
        post_content.send_keys(message)

        post_button = self.wait.until(
            EXC.element_to_be_clickable((By.XPATH, '//*[@id="modal-post-btn"]'))
        )
        post_button.click()


def main():
    speed_bot = InternetSpeedYBot()
    speed_bot.get_internet_speed()

    if speed_bot.down < PROMISED_DOWN or speed_bot.up < PROMISED_UP:
        message = f"Hey {os.environ.get('ISP_HANDLE')}, why is my internet speed {speed_bot.down}down/{speed_bot.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        speed_bot.tweet_at_provider(message)


if __name__ == "__main__":
    main()
