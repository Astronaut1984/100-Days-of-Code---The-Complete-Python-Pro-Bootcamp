from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/fake-newsletter-signup/index.html")
driver.maximize_window()

# Get Elements
fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
submit = driver.find_element(
    By.CSS_SELECTOR, value="#signup-form > .btn.btn-lg.btn-primary.btn-block"
)

fname.send_keys("selenium")
lname.send_keys("JR")
email.send_keys("selenium@jr.com")
submit.click()
