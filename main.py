from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

for row in sheet_data:

    if len(row["iataCode"]) == 0:
        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.update_data(row)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.search_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        tomorrow,
        six_month_from_today
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            text=f"Low price alert! Only £{flight.price} "
                 f"to fly from {flight.origin_city}-{flight.origin_airport} "
                 f"to {flight.destination_city}-{flight.destination_airport}, "
                 f"from {flight.depart_date} to {flight.return_date}."
        )
