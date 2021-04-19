from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

# Ask user to join the Flight Club
print("Welcome to Namsom's Flight Club.\nWe find the best flight deals and email you.")
fname = input("What is your first name?: ")
lname = input("What is your last name?: ")
email = input("What is your email?: ")
retype_email = input("Type your email again: ")
while not email == retype_email:
    email = input("Email not match. What is your email?: ")
    retype_email = input("Type your email again: ")
print("You're in the club!")

data_manager.add_user(fname.title(), lname.title(), email)

for row in sheet_data:

    if len(row["iataCode"]) == 0:
        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.update_destination_code(row)

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
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.depart_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        print(f"Message: {message}")

        # Send by SMS
        notification_manager.send_sms(message)

        # Send by email
        users = data_manager.get_customer_email()
        emails = [row["email"] for row in users]
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.depart_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_email(emails, message, link)


