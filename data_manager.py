# This class is responsible for talking to the Google Sheet. #

import requests
import os

TOKEN = os.environ.get("TOKEN")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
HEADER = {
    "Authorization": f"Bearer {TOKEN}"
}


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(f"{SHEET_ENDPOINT}/prices", headers=HEADER)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_code(self, row):
        body = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }
        response = requests.put(f"{SHEET_ENDPOINT}/prices/{row['id']}", headers=HEADER, json=body)
        response.raise_for_status()

    def add_user(self, fname, lname, email):
        body = {
            "user": {
                "firstName": fname,
                "lastName": lname,
                "email": email,
            }
        }
        response = requests.post(f"{SHEET_ENDPOINT}/users", headers=HEADER, json=body)
        response.raise_for_status()

    def get_customer_email(self):
        response = requests.get(f"{SHEET_ENDPOINT}/users", headers=HEADER)
        response.raise_for_status()
        self.customer_data = response.json()["users"]
        return self.customer_data
