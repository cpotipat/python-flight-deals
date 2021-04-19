# This class is responsible for structuring the flight data. #

class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, depart_date, return_date, stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.depart_date = depart_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
