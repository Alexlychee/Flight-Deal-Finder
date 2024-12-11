import os
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv

SHEETY_URL_ENDPOINT = os.getenv("ENV_SHEETY_URL")

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASS"]
        self._authorization = HTTPBasicAuth(self.user, self.password)
        self.sheet_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_URL_ENDPOINT)
        data = response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data

    def update_destination_data(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_URL_ENDPOINT}/{city["id"]}", json=new_data)
            print(response.text)
