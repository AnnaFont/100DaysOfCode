# Selenium Webdriver - can interact with the browser and click anywhere in the screen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Keep Chrome open when the program ends
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

# Open the website with the configuration
driver = webdriver.Chrome(options=chrome_opt)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find method to print number of articles - use the id article count and print the 1st anchor tag
num_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(num_articles.text)

# to click something in the screen
num_articles.click()

# type something in the search bar
# it can be identified by name
search = driver.find_element(By.NAME, value="search")
# Text will be text to write and it will apply enter
search.send_keys("Text to write", Keys.ENTER)

# driver.quit()
