import requests
from pprint import pprint

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    response = requests.get(url="https://api.sheety.co/f83f5bdcf3c2f74a3d16e3a94425ffca/flightDeals/prices")
    data = response.json()
    sheet_data = data["prices"]
    print(sheet_data)

