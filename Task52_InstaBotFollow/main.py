# Automatic followers
# Selenium Webdriver - can interact with the browser and click anywhere in the screen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Exceptions when you try to follow and you were already following it
from selenium.common.exceptions import ElementClickInterceptedException

import math
import time

# Insta account - TO BE MODIFIED WITH YOUR OWN ACCOUNT
INSTA_ACCOUNT = "bot_test64"
# INSTA ACCOUNT PASSWORD - TO BE MODIFIED WITH YOUR OWN PASSWORD
INSTA_PASS = "test_instagram_pass"
# Account to steal the followers - TO BE MODIFIED DEPENDING ON THE ACCOUNT NEEDED
INSTA_SIMILAR_ACCOUNT = "hiveclimbingwpg"
# Approximate number of followers - TO BE MODIFIED DEPENDING ON THE ACCOUNT FOLLOWERS NUMBER
INSTA_SIMILAR_NUM_FOLLOWERS = 50


class InstaFollower:

    def __init__(self):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(5)

        # Check if the cookie warning is present on the page
        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning[0].click()

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(INSTA_ACCOUNT)
        password.send_keys(INSTA_PASS)

        time.sleep(3)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

    def find_followers(self):
        # Open the account
        url = "https://www.instagram.com/" + INSTA_SIMILAR_ACCOUNT + "/followers"
        self.driver.get(url)

        time.sleep(3.5)
        value_css_followers = "ul li div a[href='/" + INSTA_SIMILAR_ACCOUNT + "/followers/']"
        followers = self.driver.find_element(By.CSS_SELECTOR, value=value_css_followers)
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element(By.CSS_SELECTOR, value=".xyi19xy")
        times_to_scroll = math.floor(INSTA_SIMILAR_NUM_FOLLOWERS / 15)
        for i in range(times_to_scroll):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.XPATH, '//button[contains(., "Follow")]')
        time.sleep(2)
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
                # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                print("Could not click button, skipping...")
                #cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                #cancel_button.click()
                #ok_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Ok')]")
                #ok_button.click()
                continue



#/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[28]/div/div/div/div[3]/div/button
#/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[27]/div/div/div/div[3]/div/button
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
