# This class is responsible for talking to the Google Sheet. #

import requests
import os

TOKEN = os.environ.get("TOKEN")
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        header = {
            "Authorization": f"Bearer {TOKEN}"
        }

        response = requests.get(sheet_endpoint, headers=header)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_data(self, row):
        header = {
            "Authorization": f"Bearer {TOKEN}"
        }

        body = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }
        response = requests.put(f"{sheet_endpoint}/{ row['id']}", headers=header, json=body)
        response.raise_for_status()
