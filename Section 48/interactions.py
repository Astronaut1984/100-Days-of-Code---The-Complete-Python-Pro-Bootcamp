from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

articles = driver.find_element(By.ID, value="mwDw")
print(articles.text)

# articles.click()

search_input = driver.find_element(By.NAME, value="search")
search_input.send_keys("Hello World")
search_input.send_keys(Keys.ENTER)
