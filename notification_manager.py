import os
from dotenv import load_dotenv
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.
load_dotenv()

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER_FROM"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER_TO"]
        )
        # Prints if successfully sent.
        print(message.sid)