"""This script contains all useful helpers."""
import json
import re
import requests
from requests.exceptions import HTTPError
from sqlalchemy import insert

def get_data(endpoint, headers={}):
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        return response.json()
    except HTTPError as e:
        if response.status_code == 404:
            print(f"404 Error: Resource not found for URL: {endpoint}")
        else:
            print(f"HTTP Error: {e}")
        return None  # Return None for error responses
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return None

def send_data_to_endpoint(url, data, headers=None):
    """
    Send JSON data to an endpoint using a POST request.

    :param url: The URL of the endpoint to send the data to.
    :param data: The data to send as a JSON payload (a dictionary).
    :param headers: (Optional) Additional headers to include in the request.
    :return: The response object from the server.
    """
    try:
        json_data = json.dumps(data)
        headers = headers or {'Content-Type': 'application/json'}
        response = requests.post(url, data=json_data, headers=headers)
        # response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
