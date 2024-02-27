# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# URL = 'https://www.linkedin.com/search/results/people/?keywords=devops%20engineer&origin=CLUSTER_EXPANSION&page=3&searchId=ddee30bb-e290-4399-b2d4-68dffd679c2c&sid=RkJ'
# HEADERS = {'User-Agent': 'your_user_agent', 'Accept-Language': 'en-US, en;q=0.5'}  # replace 'your_user_agent' with your actual user agent
# webpage = requests.get(URL, headers=HEADERS)

# # Parse the content of the request
# soup = BeautifulSoup(webpage.content, 'html.parser')

# # Print the HTML content
# print(soup.prettify())
# Importing the necessary libraries
from selenium import webdriver

# Create an instance of the Chrome web driver
driver = webdriver.Chrome('/home/chordify/.local/lib/python3.6/site-packages/chromedriver_autoinstaller/120/chromedriver')

# Navigate to the LinkedIn login page
driver.get('https://www.linkedin.com/login')

# Locate the username/email and password input fields
username_field = driver.find_element_by_id('username')
password_field = driver.find_element_by_id('password')

# Enter the username/email and password
username_field.send_keys('ksathira5111997@gmail.com')
password_field.send_keys('Athiraks@7560')

# Find and click the login button
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()