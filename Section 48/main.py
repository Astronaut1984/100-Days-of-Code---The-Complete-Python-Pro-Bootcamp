from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pprint import pp

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

events_titles = driver.find_elements(
    By.CSS_SELECTOR, value=".event-widget > .shrubbery > .menu > li > a"
)
events_titles = [title.text for title in events_titles]
events_dates = driver.find_elements(
    By.CSS_SELECTOR, value=".event-widget > .shrubbery > .menu > li > time"
)
events_dates = [date.get_attribute("datetime").split("T")[0] for date in events_dates]

req = {}

for i in range(len(events_titles)):
    req[i] = {"time": events_dates[i], "name": events_titles[i]}

pp(req)

driver.close()
