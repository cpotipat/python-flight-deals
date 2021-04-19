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
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=body)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            depart_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

