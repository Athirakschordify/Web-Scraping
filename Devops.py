from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup, Comment
import pandas as pd
import requests


HEADERS = {'User-Agent': 'your_user_agent', 'Accept-Language': 'en-US, en;q=0.5'}  # replace 'your_user_agent' with your actual user agent
def solve_captcha_manually():
    input("Please solve the CAPTCHA manually and press Enter when done.")

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

# Wait for the login to complete (you may need to adjust the wait conditions as needed)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'some_element_id')))
except:
    solve_captcha_manually()

# List of URLs to extract data from
urls = [
    'https://www.linkedin.com/search/results/people/?keywords=devops%20engineer&origin=CLUSTER_EXPANSION&searchId=d70b003e-6fa0-4593-a52e-e972fd4bb456&sid=YbU',
    #  'https://www.linkedin.com/search/results/people/?keywords=devops%20engineer&origin=CLUSTER_EXPANSION&page=2&searchId=d70b003e-6fa0-4593-a52e-e972fd4bb456&sid=u9t',
    #  'https://www.linkedin.com/search/results/people/?keywords=devops%20engineer&origin=CLUSTER_EXPANSION&page=3&searchId=d70b003e-6fa0-4593-a52e-e972fd4bb456&sid=mH%40',
]

# Extract data from each URL
modified_text_list = []
href_list = []

for url in urls:
    driver.get(url)

    # Extract the HTML content of the search results page after login
    search_results_html = driver.page_source
    soup = BeautifulSoup(search_results_html, 'html.parser')

    target_elements = soup.find_all(class_='HtGQzDIkdLrxVtSXBBWhGzJjOwRzdMOoCTo')

    # for target_span in target_elements:
    #     visually_hidden_class = target_span.find(class_='visually-hidden')
    #     if visually_hidden_class:
    #         span_text_content = visually_hidden_class.text.strip()
    #         text_to_remove = ["View", "’s profile"]
    #         for text in text_to_remove:
    #             span_text_content = span_text_content.replace(text, "")
    #             span_text_content = span_text_content.replace('’ profile', '')
    #         # print(span_text_content.strip())
    #         modified_text_list.append(span_text_content.strip())

    target_elements = soup.find_all(class_='t-roman t-sans')
    for target_element in target_elements:
        a_tags = target_element.find_all("a", class_="app-aware-link")
        for a_tag in a_tags:
            href_value = a_tag.get("href")
            # print(href_value)
            href_list.append(href_value)
print(href_list)


        
    # print(profile_soup)

        








# df = pd.DataFrame({'Name': modified_text_list, 'URL': href_list})
# df.to_excel('extracted_data.xlsx', index=False)










# Close the browser
driver.quit()
     
