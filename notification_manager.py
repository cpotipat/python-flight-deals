# This class is responsible for sending notifications with the deal flight details. #

from twilio.rest import Client
import os

TOKEN = os.environ.get("TOKEN")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

class NotificationManager:
    def __init__(self):
        pass