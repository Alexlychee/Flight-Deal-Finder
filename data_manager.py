import requests
from pprint import pprint

SHEETY_URL_ENDPOINT = "https://api.sheety.co/f83f5bdcf3c2f74a3d16e3a94425ffca/flightDeals/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
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
