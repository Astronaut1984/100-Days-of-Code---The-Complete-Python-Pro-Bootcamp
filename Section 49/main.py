import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXC
from selenium.common.exceptions import TimeoutException
import os

# Constants
CONFIG = dotenv.dotenv_values()
ACCOUNT_EMAIL = CONFIG["EMAIL"]
ACCOUNT_PASSWORD = CONFIG["PASS"]
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


def retry(func, retries=10, description=None):
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

    password_input
    password_input.send_keys(ACCOUNT_PASSWORD)
    submit_button.click()

    wait.until(EXC.presence_of_all_elements_located((By.ID, "schedule-page")))


def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(
        lambda _: booking_button.text == "Booked" or booking_button.text == "Waitlisted"
    )

retry(login, description="login")

# Book The 6 PM Tuesday/Thursday Class
class_cards = wait.until(
    EXC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='class-card-']"))
)

booked_counter = 0
waitlisted_counter = 0
already_booked_counter = 0
days = ["Tue", "Thu"]
detailed_class_list = []
verify = []

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(
        By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]"
    )
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday
    for day in days:
        if day in day_title:
            # Check if this is a 6pm class
            time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
            if "6:00 PM" in time_text:
                # Get the class name
                class_name = card.find_element(
                    By.CSS_SELECTOR, "h3[id^='class-name-']"
                ).text
                verify.append(
                    {
                        "title": class_name,
                        "day": day,
                        "time": " ".join(time_text.split()[1:]),
                    }
                )
                # Find and click the book button
                button = card.find_element(
                    By.CSS_SELECTOR, "button[id^='book-button-']"
                )
                if button.text == "Booked":
                    print(f"✓ Already booked: {class_name} on {day_title}")
                    already_booked_counter += 1
                    continue
                elif button.text == "Waitlisted":
                    print(f"✓ Already on waitlist: {class_name} on {day_title}")
                    already_booked_counter += 1
                    continue
                elif button.text == "Join Waitlist":
                    message = "Joined waitlist for"
                    desc = "Waitlisting"
                    waitlisted_counter += 1
                    detailed_class_list.append(
                        f"[New Waitlist] {class_name} on {day_title}"
                    )
                else:
                    message = "Booked"
                    desc = "Booking"
                    booked_counter += 1
                    detailed_class_list.append(
                        f"[New Booking] {class_name} on {day_title}"
                    )
                retry(lambda: book_class(button), description=desc)
                print(f"{message}: {class_name} on {day_title}")

# print("\n--- BOOKING SUMMARY ---")
# print(f"Classes booked: {booked_counter}")
# print(f"Waitlists joined: {waitlisted_counter}")
# print(f"Already booked/waitlisted: {already_booked_counter}")
# print(
#     f"Total Tuesday 6pm classes processed: {booked_counter + waitlisted_counter + already_booked_counter}"
# )

expected = booked_counter + waitlisted_counter + already_booked_counter
print(f"\n--- Total Tuesday/Thursday 6pm classes: {expected} ---")

# Go to "My Bookings" Link
def get_bookings():
    my_bookings = driver.find_element(By.ID, value="my-bookings-link")
    retry(my_bookings.click)

    booked_cards = wait.until(
        EXC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='booking-card-']"))
    )

    booked_cards += wait.until(
        EXC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='waitlist-card-']"))
    )

    if not booked_cards:
        raise TimeoutException("No bookings found on the My Bookings page.")
    return booked_cards

booked_cards = retry(get_bookings, description="navigating to My Bookings page")

found = 0
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
for card in booked_cards:
    title = card.find_element(By.TAG_NAME, value="h3")
    date = card.find_element(By.TAG_NAME, value="p")
    for class_ in verify:
        if (
            class_["title"] in title.text
            and class_["day"] in date.text
            and class_["time"] in date.text
        ):
            print(f"✓ Verified: {title.text}")
            found += 1

print("\n--- VERIFICATION RESULT ---")
print(f"Expected: {expected}")
print(f"Found: {found}")
if expected == found:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {expected - found} bookings")

# if detailed_class_list:
#     print("\n--- DETAILED CLASS LIST ---")
#     for message in detailed_class_list:
#         print(f"\t• {message}")
# else:
#     print("\n No New Bookings")

driver.close()
