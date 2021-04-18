# This class is responsible for talking to the Flight Search API. #

import requests
import os

TOKEN = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:

    def get_destination_code(self, city):
        code = "TESTING"  # Return "TESTING" for now to make sure Sheety is working.
        return code
