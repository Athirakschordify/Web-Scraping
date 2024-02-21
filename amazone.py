from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page=10'
HEADERS = {'User-Agent': 'your_user_agent', 'Accept-Language': 'en-US, en;q=0.5'}  # replace 'your_user_agent' with your actual user agent
webpage = requests.get(URL, headers=HEADERS)

# Parse the content of the request
soup = BeautifulSoup(webpage.content, 'html.parser')

# Find and print the names and prices of the mobiles
mobiles = []

name_elements = soup.find_all('div', class_='_4rR01T')
price_elements = soup.find_all('div', class_='_30jeq3')

for name, price in zip(name_elements, price_elements):
    mobiles.append({
        'Name': name.text.strip(),
        'Price': price.text.strip()
    })

# Create a DataFrame from the extracted data
df1 = pd.DataFrame(mobiles)

# Save the DataFrame to CSV
df1.to_csv('mobile_data10.csv', index=False)

# Save the DataFrame to JSON
df1.to_json('mobile_data10.json', orient='records', lines=True)
df1.to_excel('mobile_data10.xlsx', index=False)

# Print the DataFrame
print(df1)
