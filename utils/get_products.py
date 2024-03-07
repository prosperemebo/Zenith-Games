import json
import time
from os import getenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from functions import get_data, send_data_to_endpoint

load_dotenv()

def get_product_page_soup(product_url, chrome_options):
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get(product_url)
        
        driver.implicitly_wait(10)

        product_page_source = driver.page_source
        product_page_soup = BeautifulSoup(product_page_source, 'html.parser')
    
    return product_page_soup


def handle_data(products):
    api_url = getenv("API_URI")
    post_url = f"{api_url}/api/v1/products"
    
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')

    for product_data in products:
        print(product_data.get('link'))
        
        # Extract Data
        title_dict = product_data.get('title')
        content_dict = product_data.get('content')
        excerpt_dict = product_data.get('excerpt')
        category_list = product_data.get('product_cat')

        # Parse Summary
        excerpt_soup = BeautifulSoup(excerpt_dict.get('rendered'), 'html.parser')
        excerpt_paragraph = excerpt_soup.find('p').get_text(strip=True) if excerpt_soup.find('p') else ""
        
        # Scrape Data from web page using Selenium
        product_url = product_data.get('link')
        product_page_soup = get_product_page_soup(product_url, chrome_options)
        
        # Continue with the rest of your code using product_page_soup
        # For example, extracting the price and images

        # Extract Price
        price_span = product_page_soup.find('span', class_='woocommerce-Price-amount')
        price_text = price_span.text.strip()
        price_number = int(price_text.replace('₦', '').replace(',', ''))

        # Extract Image URLS
        image_divs = product_page_soup.find_all('div', class_='woocommerce-product-gallery__image')
        product_images = [div['data-thumb'] for div in image_divs]

        # Parse Categoriy list with the category as stored in DB
        category_ids = []
        
        for product_category_source_id in category_list:
            parent_dict_url = f'http://localhost:8000/api/v1/categories?source_id={product_category_source_id}'
            category = get_data(parent_dict_url)
            
            if category is not None and len(category) > 0:
                first = category[0]
                category_ids.append(first.get('id'))
                
            time.sleep(1)
            
        image_urls = product_images[1:] if len(product_images) > 1 else []
                
        # Create product dict
        product_dict = {
            "label": title_dict.get("rendered"),
            "slug": product_data.get("slug"),
            "summary": excerpt_paragraph,
            "description": content_dict.get("rendered"),
            
            "cover_image": product_images[0] if product_images else None,
            "images": ','.join(image_urls),
            "price": price_number,
            
            "source_id": product_data.get("id"),
            "categories": ','.join(category_ids),
        }
                
        print(f'Saving {title_dict.get("rendered")} to DB')
        print('___________________________________________________')
        response = send_data_to_endpoint(post_url, product_dict)

        if response is not None:
            try:
                status_code = response.status_code
                response_data = response.json()

            except json.JSONDecodeError:
                print(f'Error occurred while saving {title_dict.get("rendered")} to DB')
                print('------------------------------------------------------')

        time.sleep(1)


def main(parent_id=0):
    page = 1
    per_page = 100
    is_next_page = True
    
    # GET PRODUCTS FROM API
    api_url = getenv("API_URI")
    products_url = f"{api_url}/api/v1/products?page={page}&per_page=1000"
    api_products = get_data(products_url)

    while is_next_page == True:
        # GET PRODUCTS FROM CHEAP GAMES NG
        url = f"https://www.cheapgamesng.com/wp-json/wp/v2/product?page={page}&per_page={per_page}&parent={parent_id}"
        products = get_data(url)

        if products is None or api_products is None:
            print("Failed to get data! Bye...")
            return

        if len(products) == 0:
            is_next_page = False
        else:
            page += 1
            
        # FILTER PRODUCTS IN DATABASE
        api_products_source_ids = [product.get("source_id") for product in api_products]
        filtered_products = []
        
        for product in products:
            if str(product.get("id")) not in api_products_source_ids:
                filtered_products.append(product)

        handle_data(filtered_products)


if __name__ == "__main__":
    main()
