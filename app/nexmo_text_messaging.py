import os

from nexmo import Client, ClientError, AuthenticationError, ServerError
from dotenv import load_dotenv

load_dotenv()

NEXMO_KEY: str = os.getenv("NEXMO_KEY")
NEXMO_SECRET: str = os.getenv("NEXMO_SECRET")
SENDER_NAME: str = os.getenv("SENDER_NAME")
TO_NUMBER: str = os.getenv("TO_NUMBER")


def get_nexmo_client() -> Client:
    try:
        nexmo_client: Client = Client(key=NEXMO_KEY, secret=NEXMO_SECRET)
        return nexmo_client
    except (ClientError, AuthenticationError) as nexmo_error:
        print(f"Exception Occurred: {nexmo_error}")
        raise nexmo_error


def send_message():
    client = get_nexmo_client()
    try:
        response_data = client.send_message(
            {
                "from": SENDER_NAME,
                "to": TO_NUMBER,
                "text": "Hello message from Nexmo",
            }
        )

        if response_data["messages"][0]["status"] == "0":
            print("Message sent successfully")
        else:
            print(
                f"Message failed with error: {response_data['messages'][0]['error-text']}"
            )
    except ServerError as server_error:
        print(f"Exception Occurred: {server_error}")


if __name__ == "__main__":
    send_message()
