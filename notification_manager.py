# This class is responsible for sending notifications with the deal flight details. #

from twilio.rest import Client
import os

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, text):
        message = self.client.messages.create(
            body=text,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
