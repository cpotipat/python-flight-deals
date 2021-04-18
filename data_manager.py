# This class is responsible for talking to the Google Sheet. #

import requests


class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_data(self, endpoint, token):
        header = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(endpoint, headers=header)
        response.raise_for_status()
        self.sheet_data = response.json()

    def update_data(self, endpoint, token, text):
        header = {
            "Authorization": f"Bearer {token}"
        }

        body = {
            "price": {
                "iataCode": text
            }
        }
        response = requests.put(endpoint, headers=header, json=body)
        response.raise_for_status()
