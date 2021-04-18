from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from pprint import pprint
import os

TOKEN = os.environ.get("TOKEN")
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

data_manager = DataManager()
data_manager.get_data(sheet_endpoint, TOKEN)
sheet_data = data_manager.sheet_data["prices"]

for item in range(len(sheet_data)):
    each_row = sheet_data[item]

    if len(each_row["iataCode"]) == 0:
        flight_search = FlightSearch()
        code = flight_search.get_destination_code(each_row["city"])
        data_manager.update_data(f"{sheet_endpoint}/{each_row['id']}", TOKEN, code)

pprint(sheet_data)




