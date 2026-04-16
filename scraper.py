import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://pk.ethnc.com/collections/rozana?page=1"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
time.sleep(2)

soup = BeautifulSoup(response.text, 'html.parser')
product_cards = soup.find_all('div', class_='card-wrapper')

all_products = []

for card in product_cards:
    name_tag = card.find('h3', class_='card__heading')
    name = name_tag.get_text(strip=True) if name_tag else "N/A"

    price_tag = card.find('span', class_='money')
    price = price_tag.get_text(strip=True) if price_tag else "N/A"

    img_tag = card.find('img')
    img_url = "No Image"
    if img_tag:
        source = img_tag.get('src') or img_tag.get('data-src')
        if source:
            img_url = 'https:' + source if source.startswith('//') else source

    all_products.append({
        'Product Name': name,
        'Price': price,
        'Image Link': img_url
    })

print(f"Scraped {len(all_products)} products successfully.")