from pyfcm import FCMNotification
from pydantic import BaseModel
import os
from dotenv import load_dotenv

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
