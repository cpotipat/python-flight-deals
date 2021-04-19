from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

for row in sheet_data:

    if len(row["iataCode"]) == 0:
        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.update_data(row)

print(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.search_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        tomorrow,
        six_month_from_today
    )





