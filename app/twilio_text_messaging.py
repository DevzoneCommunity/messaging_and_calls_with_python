import os

from twilio.base.exceptions import TwilioException
from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TO_NUMBER = os.getenv("TO_NUMBER")
TWILIO_FROM = os.getenv("TWILIO_FROM")

try:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    response = client.messages.create(
        body="Hello, message from Twilio", from_="+12056351684", to="+919677758721"
    )
    print(response.sid)
except TwilioException as twilio_exception:
    print(f"Exception Occurred: {twilio_exception}")
