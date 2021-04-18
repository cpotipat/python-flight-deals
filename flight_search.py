# This class is responsible for talking to the Flight Search API. #

import requests
import os


TOKEN = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"


class FlightSearch:

    def get_destination_code(self, city):
        header = {
            "apikey": TOKEN
        }

        body = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
        }

        response = requests.get(TEQUILA_ENDPOINT, headers=header, params=body)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code
