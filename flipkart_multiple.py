from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.drawing.image import Image as ExcelImage
from io import BytesIO

def scrape_mobile_data(url):
    HEADERS = {'User-Agent': 'your_user_agent', 'Accept-Language': 'en-US, en;q=0.5'}
    webpage = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, 'html.parser')

    mobiles = []
    name_elements = soup.find_all('div', class_='_4rR01T')
    price_elements = soup.find_all('div', class_='_30jeq3')
    image_elements = soup.find_all('img', class_='_396cs4')

    for name, price, image in zip(name_elements, price_elements, image_elements):
        mobiles.append({
            'Name': name.text.strip(),
            'Price': price.text.strip(),
            'Image': image['src'].strip()
        })

    df = pd.DataFrame(mobiles)
    return df

def download_image(url):
    response = requests.get(url)
    img = BytesIO(response.content)
    return img

# List of URLs to scrape
urls = [
    'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page=10',
    'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page=9'
]

# Scrape data from each URL and concatenate the results into a single DataFrame
all_mobiles = pd.concat([scrape_mobile_data(url) for url in urls], ignore_index=True)

# Create an Excel workbook and add a worksheet
wb = Workbook()
ws = wb.active

# Add data from the DataFrame to the worksheet
for row in dataframe_to_rows(all_mobiles, index=False, header=True):
    ws.append(row)

# Add images to the worksheet
for index, row in all_mobiles.iterrows():
    img_data = download_image(row['Image'])
    img = ExcelImage(img_data)
    ws.add_image(img, f'D{index + 2}')  # Assuming 'Image' column is in column D

# Save the Excel file
wb.save('all_mobile_data_with_images.xlsx')
