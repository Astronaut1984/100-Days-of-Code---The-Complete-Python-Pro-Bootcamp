import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXC
from selenium.common.exceptions import TimeoutException
import os

# Constants
CONFIG = dotenv.dotenv_values()
ACCOUNT_EMAIL = CONFIG["ADMIN_EMAIL"]
ACCOUNT_PASSWORD = CONFIG["ADMIN_PASS"]
GYM_URL = CONFIG["GYM_URL"]

# Load chrome options with persistent user profile
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome-profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# Initialize a driver instance
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver=driver, timeout=2)


def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            driver.implicitly_wait(1)


# Login Functionality
def login():
    login_btn = wait.until(EXC.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(EXC.presence_of_element_located((By.ID, "email-input")))
    password_input = wait.until(
        EXC.presence_of_element_located((By.ID, "password-input"))
    )
    submit_button = wait.until(
        EXC.presence_of_element_located((By.ID, "submit-button"))
    )

    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)
    submit_button.click()

    wait.until(EXC.presence_of_all_elements_located((By.ID, "schedule-page")))


retry(login, description="login")
