import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXC
from selenium.common import exceptions
import time
import os

dotenv.load_dotenv()


def init_browser() -> webdriver.Chrome:
    # Load chrome options with persistent user profile
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # Initialize a driver instance
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(os.environ.get("TINDOG_URL"))

    return driver


def login(driver: webdriver.Chrome, wait: WebDriverWait):
    login_button = wait.until(
        EXC.element_to_be_clickable((By.XPATH, "/html/body/header/button"))
    )
    login_button.click()

    # Login with FB
    fb_login_button = wait.until(
        EXC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div/div/button[1]")
        )
    )
    fb_login_button.click()

    # Switch to FB login page
    fb_window = driver.window_handles[1]
    driver.switch_to.window(fb_window)

    email_input = wait.until(EXC.element_to_be_clickable((By.ID, "email")))
    password_input = wait.until(EXC.element_to_be_clickable((By.ID, "pass")))

    # Send login details
    email_input.clear()
    email_input.send_keys(os.environ.get("USER_EMAIL"))
    password_input.clear()
    password_input.send_keys(os.environ.get("USER_PASSWORD"))
    submit_button = wait.until(
        EXC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/form/button"))
    )
    submit_button.click()


def swipe_right(driver: webdriver.Chrome, wait: WebDriverWait):
    back_to_tindog = "/html/body/main/div[3]/a"
    like_button = wait.until(
        EXC.element_to_be_clickable(
            (By.XPATH, '//*[@id="like-button-container"]/form/button')
        )
    )

    while True:
        try:
            like_button = wait.until(
                EXC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="like-button-container"]/form/button')
                )
            )
            like_button.click()
            time.sleep(1)
        except exceptions.NoSuchElementException as e:
            print("Like button not found")
        except exceptions.ElementClickInterceptedException:
            back_to_tindog_button = wait.until(
                EXC.element_to_be_clickable((By.XPATH, back_to_tindog))
            )
            back_to_tindog_button.click()
        except exceptions.TimeoutException:
            print("Done Swiping for today :)")
            break


def dismiss_requests(driver: webdriver.Chrome, wait: WebDriverWait):
    main_window = driver.window_handles[0]
    driver.switch_to.window(main_window)

    allow_location = wait.until(
        EXC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button"))
    )
    allow_location.click()
    dismiss_notifications = wait.until(
        EXC.element_to_be_clickable(
            (By.XPATH, "/html/body/main/div/div/form/button[2]")
        )
    )
    dismiss_notifications.click()
    accept_cookies = wait.until(
        EXC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button"))
    )
    accept_cookies.click()


def main():
    driver = init_browser()
    wait = WebDriverWait(driver=driver, timeout=2)

    login(driver, wait)
    dismiss_requests(driver, wait)
    swipe_right(driver, wait)


if __name__ == "__main__":
    main()
