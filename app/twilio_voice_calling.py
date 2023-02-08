import os

from twilio.rest import Client, TwilioException

from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TO_NUMBER = os.getenv("TO_NUMBER")
TWILIO_FROM = os.getenv("TWILIO_FROM")

try:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    response = client.calls.create(
        url="http://demo.twilio.com/docs/voice.xml",
        to=TO_NUMBER,
        from_=TWILIO_FROM,
    )
    print(response.sid)
except TwilioException as twilio_exception:
    print(f"Exception Occurred: {twilio_exception}")
