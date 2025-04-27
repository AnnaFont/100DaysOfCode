# Selenium Webdriver - can interact with the browser and click anywhere in the screen
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open when the program ends
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

# Open the website with the configuration
driver = webdriver.Chrome(options=chrome_opt)
driver.get("https://www.amazon.es/La-Sportiva-30A402602-La-sportiva/dp/B085G5RG7M/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%"
           "C5%BD%C3%95%C3%91&dib=eyJ2IjoiMSJ9.dxulxgVqZfExkz6G5llRA1NvyTet7W7v20C_xRIP4q655moRciB5NVMUwnUMIDpvi5RuGNw1"
           "aXAsbN7GNzupnMKGwLL22wgfNSh5Ij3WH_JmcNNZjHByxVA5UXCbAI6o-GrCLD6YSNcOCpvptr8S6zOzcdZ4i59Q-OiWHHyiqdZpMHNt2wB"
           "8pP21Jr43a29h2ZjyZA1HK-rEUBebcshUOgLKgtbGmpJAbHBezX5VSB-3uK-21QQHOcyK7yZ23bsx996tO5coswMawTmZeF-WqoZjmCjMCJ"
           "Cc7h05SNB-aO4.NeiJW0r1OuK4NAcLY9nH4nzwjkWWJrckvN6Tivj0HWc&dib_tag=se&keywords=la%2Bsportiva%2Bsolution&qid="
           "1745783992&s=sports&sr=1-3&th=1&psc=1")

# Take the price - it is much faster than with Beautiful soup
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"Price: ${price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org/")

# Find method to find all the upcoming elements
time_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
text_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range((len(time_events))):
    events[n] = {
        "time": time_events[n].text,
        "text": text_events[n].text,
    }

print(events)
# Close is for a tab
# driver.close()
# Quit is for the entire browser
driver.quit()