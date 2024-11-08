from pyfcm import FCMNotification
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import requests

load_dotenv()


class PushNotificationPayload(BaseModel):
    title: str
    body: str
    token: str


firebase_service = FCMNotification(
    service_account_file=os.getenv("FCM_SERVICE_ACCOUNT_FILE"),
    project_id=os.getenv("FCM_PROJECT_ID"),
)
firebase_service.api_key = os.getenv("FCM_API_KEY")


def send_push_notification_firebase(token: str, title: str, message: str):
    result = firebase_service.notify(
        fcm_token=token,
        notification_title=title,
        notification_body=message,
    )
    return result


def send_push_notification_expo(token: str, title: str, message: str):
    expo_url = os.getenv("EXPO_NOTIFICATION_URL")

    headers = {
        "content-type": "application/json",
    }

    payload = {
        "to": token,
        "title": title,
        "body": message,
    }

    response = requests.post(expo_url, headers=headers, json=payload)

    if response.status_code != 200:
        print("Error sending notification:", response.status_code, response.text)

    return response.json()
