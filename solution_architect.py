from selenium.webdriver.common.keys import Keys  # Add this import for sending special keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

# Install the appropriate version of chromedriver if necessary
chromedriver_autoinstaller.install()

# Use chromedriver for Selenium
driver = webdriver.Chrome()

# Navigate to the login page
driver.get('https://www.linkedin.com/login')

# Wait for the username and password fields to be visible
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'username')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))

# Enter login credentials
username_field.send_keys('ksathira5111997@gmail.com')
password_field.send_keys('Athiraks@7560' + Keys.RETURN)  # Send Enter key to submit

# Wait for the login process to complete
try:
    WebDriverWait(driver, 10).until(EC.url_contains('linkedin.com/feed/'))
    
    # Define multiple target URLs
    target_urls = [
        'https://www.linkedin.com/search/results/people/?keywords=solution%20architect%20open%20to%20work&origin=GLOBAL_SEARCH_HEADER&sid=W%40e',
        # 'https://www.linkedin.com/search/results/people/?keywords=solution%20architect%20open%20to%20work&origin=CLUSTER_EXPANSION&page=2&searchId=cfab5c11-5063-4386-ad04-a7794af99a73&sid=jh%3A',
        # 'https://www.linkedin.com/search/results/people/?keywords=solution%20architect%20open%20to%20work&origin=CLUSTER_EXPANSION&page=3&searchId=cfab5c11-5063-4386-ad04-a7794af99a73&sid=T7S',
    ]

    names_list = []

    for target_url in target_urls:
        driver.get(target_url)
        target_page_html = driver.page_source
        soup = BeautifulSoup(target_page_html, 'html.parser')
        app_aware_links = soup.find_all(class_='app-aware-link')
        href_list = []

        for link in app_aware_links:
            href = link.get('href')
            href_list.append(href)

        linkedin_urls = [url for url in href_list if 'https://www.linkedin.com/in/' in url]
        unique_linkedin_urls = list(set(linkedin_urls))

        for href in unique_linkedin_urls:
            driver.get(href)
            href_soup = BeautifulSoup(driver.page_source, 'html.parser')
            target_elements = href_soup.find_all(class_='text-heading-xlarge inline t-24 v-align-middle break-words')

            for target_element in target_elements:
                content = target_element.get_text(strip=True)
                names_list.append(content)

    print(names_list)

except:
    solve_captcha_manually()  # Handle CAPTCHA manually if necessary

# Continue with the rest of your script...

