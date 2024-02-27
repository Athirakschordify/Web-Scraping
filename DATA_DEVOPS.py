import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HEADERS = {'User-Agent': 'your_user_agent', 'Accept-Language': 'en-US, en;q=0.5'}  # replace 'your_user_agent' with your actual user agent

def solve_captcha_manually():
    input("Please solve the CAPTCHA manually and press Enter when done.")

driver = webdriver.Chrome('/home/chordify/.local/lib/python3.6/site-packages/chromedriver_autoinstaller/120/chromedriver')

driver.get('https://www.linkedin.com/login')

username_field = driver.find_element_by_id('username')
password_field = driver.find_element_by_id('password')

username_field.send_keys('ksathira5111997@gmail.com')
password_field.send_keys('Athiraks@7560')

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'some_element_id')))
except:
    solve_captcha_manually()

urls = [
    'https://www.linkedin.com/search/results/people/?keywords=devops%20engineer&origin=CLUSTER_EXPANSION&searchId=d70b003e-6fa0-4593-a52e-e972fd4bb456&sid=YbU',
]

names_list = []
href_list = []

for url in urls:
    driver.get(url)

    search_results_html = driver.page_source
    soup = BeautifulSoup(search_results_html, 'html.parser')

    target_elements = soup.find_all(class_='HtGQzDIkdLrxVtSXBBWhGzJjOwRzdMOoCTo')

    target_elements = soup.find_all(class_='t-roman t-sans')
    for target_element in target_elements:
        a_tags = target_element.find_all("a", class_="app-aware-link")
        for a_tag in a_tags:
            href_value = a_tag.get("href")
            href_list.append(href_value)

# Loop through href_list and extract HTML
for href in href_list:
    driver.get(href)
    href_soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Extract content with the specified class
    import pdb; pdb.set_trace()  # Use this line instead of breakpoint()
    break
    target_elements = href_soup.find_all(class_='text-heading-xlarge inline t-24 v-align-middle break-words')

    # # print(target_element)
    # for target_element in target_elements:
    #     content = target_element.get_text(strip=True)
    #     print(content)
    #     import pdb; pdb.set_trace()  # Use this line instead of breakpoint()
    #     break
driver.quit()
