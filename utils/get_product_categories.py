import json
import time

from os import getenv
from dotenv import load_dotenv
from functions import get_data, send_data_to_endpoint

load_dotenv()


def send_data(categories):
    api_url = getenv("API_URI")
    post_url = f"{api_url}/api/v1/categories"

    for category_data in categories:
        category_dict = {
            "label": category_data.get("name"),
            "slug": category_data.get("slug"),
            "summary": category_data.get("description"),
            "source_id": category_data.get("id"),
            "parent_id": category_data.get("parent"),
        }

        if category_data.get("parent") == 0:
            del category_dict["parent_id"]
        else:
            parent_dict_url = f'http://localhost:8000/api/v1/categories?source_id={category_data.get("parent")}'
            category = get_data(parent_dict_url)
            
            if category is not None and len(category) > 0:
                first = category[0]
                category_dict["parent_id"] = first.get('id')
                

        response = send_data_to_endpoint(post_url, category_dict)

        if response is not None:
            try:
                status_code = response.status_code
                response_data = response.json()

            except json.JSONDecodeError:
                print("Failed to parse JSON response")
                
        main(category_data.get("id"))

        time.sleep(5)


def main(parent_id=0):
    page = 1
    per_page = 20
    is_next_page = True

    while is_next_page == True:
        url = f"https://www.cheapgamesng.com/wp-json/wp/v2/product_cat?page={page}&per_page={per_page}&parent={parent_id}"
        categories = get_data(url)

        if categories is None:
            print("Failed to get data! Bye...")
            return

        if len(categories) == 0:
            is_next_page = False
        else:
            page += 1

        send_data(categories)


if __name__ == "__main__":
    main()
