# This class is responsible for structuring the flight data. #

class FlightData:
    def __init__(self, data):
        self.data_list = data
        self.city = ""
        self.price = ""

    # def format_data(self):
    #     for data in self.data_list:
    #         self.city = data
