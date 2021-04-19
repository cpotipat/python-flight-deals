# This class is responsible for talking to the Flight Search API. #

import requests
import os
from flight_data import FlightData

TOKEN = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


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

        response = requests.get(f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=body)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    def search_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {
            "apikey": TOKEN
        }

        body = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=body)
        response.raise_for_status()
        print(response.json())


flight_search = FlightSearch()
flight_search.search_flight("LON", "PAR", "01/05/2021", "05/05/2021")
